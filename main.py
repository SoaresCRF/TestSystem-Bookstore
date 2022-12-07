from entities.user_interaction import UserInteraction

user_inter = UserInteraction()
opcao = user_inter.get_opcao_by_user()
while opcao:
    opcao = user_inter.get_opcao_by_user()
