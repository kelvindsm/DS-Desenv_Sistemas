from flask import Blueprint, render_template, request, current_app
from werkzeug.utils import secure_filename
import datetime
import os


from database.servico_dao import ServicoDAO
from database.Local_dao import LocalDAO
from database.Empregado_dao import EmpregadoDAO
from database.ordem_servico_dao import OrdemServicoDAO


bp_abrir = Blueprint('abrir', __name__, url_prefix='/sol/abrir')




@bp_abrir.route('/form')
def abrir_solicitacao():
   empregadoDAO = EmpregadoDAO()
   lst_empregados = empregadoDAO.read_by_filters([('sts_empregado', '=', 'A')])
   servicoDAO = ServicoDAO()
   lst_servicos = servicoDAO.read_by_filters([('sts_servico', '=', 'A')])
   localDAO = LocalDAO()
   lst_locais = localDAO.read_by_filters([('sts_local', '=', 'A')])


   return render_template('sol/abrir/form.html', lst_servicos=lst_servicos, lst_locais=lst_locais,
                          lst_empregados=lst_empregados)




@bp_abrir.route('/comprovante', methods=['POST'])
def comprovante():
   if 'arq_ordem_servico' in request.files:
       file = request.files['arq_ordem_servico']
       filename = secure_filename(file.filename)
       local_filename = os.path.join(current_app.config['UPLOAD_FOLDER'], filename)
       file.save(local_filename)


   dao = OrdemServicoDAO()
   osr = dao.new_object()


   osr.dti_ordem_servico = datetime.datetime.now()
   osr.dsc_ordem_servico = request.form['dsc_ordem_servico']
   osr.sts_ordem_servico = 'C'
   osr.jsn_atendimento_ordem_servico = {'status': 'Ordem de Serviço Aberta'}
   if 'num_patrimonio' in request.form and request.form['num_patrimonio']:
       osr.num_patrimonio = request.form['num_patrimonio']
   osr.cod_empregado = int(request.form['cod_empregado'])
   osr.cod_servico = int(request.form['cod_servico'])
   osr.cod_local = int(request.form['cod_local'])


   dao.insert(osr)


   return render_template('sol/abrir/comprovante.html', osr=osr)