from flask import Blueprint, render_template, request
from database.setor_dao import SetorDAO

bp_setor = Blueprint('setor', __name__, url_prefix='/adm/setor')


@bp_setor.route('/incluir')  # /adm/setor/incluir
def incluir():
    return render_template('adm/setor/incluir.html', msg="", css_msg="")


@bp_setor.route('/salvar_incluir', methods=['POST'])  # /adm/setor/salvar_incluir
def salvar_incluir():
    dao = SetorDAO()
    setor = dao.new_object()
    setor.sgl_setor = request.form['sgl_setor']
    setor.nme_setor = request.form['nme_setor']
    setor.eml_setor = request.form['eml_setor']
    setor.sts_setor = request.form['sts_setor']
    if dao.insert(setor):
        msg = f"Setor número {setor.idt_setor} inserido com sucesso!"
        css_msg = "sucesso"
    else:
        msg = "Erro ao tentar incluir setor!"
        css_msg = "erro"

    return render_template('adm/setor/incluir.html', msg=msg, css_msg=css_msg)
