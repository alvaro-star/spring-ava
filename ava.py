import sys
from AvaClass.Class.modelClass import create_model
from AvaClass.Class.repositoryClass import create_repository
from AvaClass.Class.serviceClass import create_service
from AvaClass.config.confReader import ConfEnv
from AvaClass.Class.resourceClass import create_resource

if __name__ == "__main__":
    if len(sys.argv)!= 3:
        print("Numero de argumentos insuficientes")
        sys.exit(1)
    [nameFile, instruction, name] = sys.argv
    
    [comand, option] = instruction.split(":")
    configEnviroment = ConfEnv()

    name = configEnviroment.set_directory_project(name)


    # Verificar se o nome da classe é válido (somente letras e começar com letra maiúscula)
    if not name.isidentifier() or not name[0].isupper():
        print("Nome da classe inválido. Use somente letras e comece com letra maiúscula.")
        sys.exit(1)

    postFixModel = configEnviroment.get_post_fix_model()
    postFixService = configEnviroment.get_post_fix_service()
    postFixRepository = configEnviroment.get_post_fix_repository()
    postFixDto = configEnviroment.get_post_fix_dto()
    # Escolhe o diretorio
    match (option):
        case "all":
            create_model(configEnviroment,name)
            create_repository(configEnviroment,name, name+postFixModel)
            create_service(configEnviroment,name, name+postFixModel, name+postFixRepository, name + postFixDto)
            create_resource(configEnviroment,name, name+postFixDto, name+postFixService)
        case "model":
            create_model(configEnviroment,name)
        case "teset":
            teste = configEnviroment.get_directory_project()
            print(teste)
        case "resource":
            create_resource(configEnviroment,name, name+postFixDto, name+postFixService)
        case "resolver":
            print("Pronto1")
        case "repository":
            create_repository(configEnviroment,name, name+postFixModel)
        case "service":
            create_service(configEnviroment,name, name+postFixModel, name+postFixRepository, name + postFixDto)


