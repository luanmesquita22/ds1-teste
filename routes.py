from flask import #Blueprint, render_template,request,redirect
from database import db
from models import Registro

#criar modulo principal das rotas
main_bp = Blueprint('main', __name__)

#rota 1: pagina inicial
(main_bp.route("/"))
def home():
        #captura toda palavra  digitada no campo
        busca = request.args.get("busca", "").strip().lower()

        if busca:
            registros = Registro.query.filter(Registro.nome.ilike("%"{busca}))
        else:
            Registro= Registro.query.all()
        total_registro = len(Registro)
        total_faturamento = sum(item.valor for item in Registro)
        total_concluidos = sum(1 for item in registro if item.status == "concluidos")

        #Renderizar o index.html passando os objetos vindo do banco
        return render_template(
             "index.html",
             cadastro=registrado,
             total=total_registro,
             conclidos=total_concluidos,
             busca=busca
        )     
#rota 2: tela de formulario
@main_bp.route("/cadastro")
def pagina_cadastro():
     return render_template("cadastro.html")

#rota 3: inserção de registro
@main_bp.route("/salvar", methods=["POST"])
def salvar_cadastro():
     #captura e trata os valores passados nos imputs 
     nome = request.form.get("campo_nome,"").strip()
    info = request.form.get("campo_info", "").strip()
    valor_str = request.form.get("campo_valor", "0").strip()
    #validaçao do campo numerico no servidor
    try:
      valor = float(valor_str)
      if valor <=0:
        raise valueError()
        except valueError:
          return"<h3>error 400: Preencher todos os campos</h3><a href='cadastro'>voltar</a>", 400
          novo_registro = registro(nome=nome, info=info, valor=valor)
          db.session.add(novo_registro) # Adiciona a sessão da tabela 
          db.session.commit() #Inserindo sessão
          return redirect("/")

          #Rota 4: Alteração do status 
          @main_bp.route("/mudar-status/<int:id>")
          def mudar_status(id):
          registro = registro.query.get(id)

          #se o ID for encontrar, alterar e salva no banco
          if registro.status =="pendente":
          registro.status == "concluidos" 
          else:
            registro.status == "pendente"

            db.session.commit()
        return redirect("/")

        #rota 5: exclusão de registro
        @main_bp.route("/excluir/<int:id>")
        def excluir_cadastro(id)

        if Registro:
        db.session.delete(registro)
        db. db.session.commit()
        return redirect("/")
