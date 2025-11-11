# Classe DAO para a entidade "tb_setor"
from database.model_dao import DAO


class OrdemServicoDAO(DAO):
    def __init__(self):
        super().__init__("tb_ordem_servico", "idt_ordem_servico")
