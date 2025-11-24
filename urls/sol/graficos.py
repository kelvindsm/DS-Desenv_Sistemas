from flask import Blueprint, render_template, request, send_file
import io
from openpyxl import Workbook
from openpyxl.styles import Font, Border, Side, PatternFill
from openpyxl.utils import get_column_letter
from database.setor_dao import SetorDAO

bp_graficos = Blueprint('graficos', __name__, url_prefix='/sol/graficos')


@bp_graficos.route('/menu')
def menu():
    return render_template('sol/graficos/menu.html')


def _dados_organograma():
    """Busca e estrutura os dados para o ECharts."""
    dao_setor = SetorDAO()

    setores = dao_setor.read_all()
    setores_nodes = []

    for setor in setores:
        servicos_nodes = []
        for servico in setor.tb_servico_collection:
            servicos_nodes.append({
                'name': servico.nme_servico + ' R$ ' + str(servico.vlr_servico),
            })
        setores_nodes.append({
            'name': setor.nme_setor + "-" + setor.sgl_setor,
            'children': servicos_nodes
        })

    return {
        'name': 'Todos os Setores',
        'children': setores_nodes
    }


@bp_graficos.route('/hierarquia')
def hierarquia():
    return render_template('sol/graficos/hierarquia.html', dados=_dados_organograma())
