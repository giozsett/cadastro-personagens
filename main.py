from interface import Interface
from bancodados import BancoDados

interface = Interface()
opcao = ""

while opcao != 0:
    interface.titulo()
    interface.menuPrincipal()
    opcao = interface.selecionarOpcao([1, 2, 3])

    if opcao == 1:
        interface.listaPersonagens()
        opcao = ""
        interface.limpaTela()

    elif opcao == 2:
        interface.cadastrarPersonagem()
        opcao = ""
        interface.limpaTela()


