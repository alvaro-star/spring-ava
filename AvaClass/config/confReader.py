import os
class ConfEnv:
    def __init__(self):
        config = {}
        filename = 'AvaClass/config/config.txt'    
        with open(filename, 'r') as file:
            for line in file:
                # Remove espaços em branco e quebras de linha
                line = line.strip()
                # Ignore linhas vazias
                if not line:
                    continue
                # Divida a linha na chave e no valor
                key, value = line.split('=', 1)
                config[key.strip()] = value.strip()
        self.config = config
        self.config['DIRECTORY_PROJECT'] = self.__generate_directory_project()
        
        if os.path.isdir(self.config['DIRECTORY_PROJECT']):
            print("existe")
        else:
            print("nao existe")
    def get_directory_src(self):
        return self.config.get("DIRECTORY_SRC")

    def get_package_code(self):
        return self.config.get("PACKAGE_CODE")

    def get_package_repositories(self):
        return self.config.get("PACKAGE_REPOSITORIES")

    def get_post_fix_repository(self):
        return self.config.get("POST_FIX_REPOSITORY")

    def get_package_models(self):
        return self.config.get("PACKAGE_MODELS")

    def get_post_fix_model(self):
        return self.config.get("POST_FIX_MODEL")

    def get_package_controllers(self):
        return self.config.get("PACKAGE_CONTROLLERS")

    def get_post_fix_controller(self):
        return self.config.get("POST_FIX_CONTROLLER")

    def get_package_resources(self):
        return self.config.get("PACKAGE_RESOURCES")

    def get_post_fix_resource(self):
        return self.config.get("POST_FIX_RESOURCE")

    def get_package_resolvers(self):
        return self.config.get("PACKAGE_RESOLVERS")

    def get_post_fix_resolver(self):
        return self.config.get("POST_FIX_RESOLVER")

    def get_package_services(self):
        return self.config.get("PACKAGE_SERVICES")

    def get_post_fix_service(self):
        return self.config.get("POST_FIX_SERVICE")

    def get_package_dtos(self):
        return self.config.get("PACKAGE_DTOS")

    def get_post_fix_dto(self):
        return self.config.get("POST_FIX_DTO")
    def get_directory_project(self):
        return self.config.get("DIRECTORY_PROJECT")
    def get_type_bd(self):
        return self.config.get("TYPE_BD")
    def __generate_directory_project(self):
        directorySrc = self.get_directory_src().split('.')
        packageFiles = self.get_package_code().split('.')
        if (len(directorySrc) == 0 or len(packageFiles) == 0):
            print("Busca do diretorio: as variaveis de ambiente não são válidas")
            return "error"
        pathFiles = directorySrc[0]
        if(len(directorySrc) > 0):
            for i in range(1, len(directorySrc)):
                pathFiles = pathFiles+"/"+directorySrc[i]
        for word in packageFiles:
            pathFiles = pathFiles+"/"+word
        return pathFiles
    
    def set_directory_project(self, name:str):
        customizedDirectory = name.split("/")
        relativePath = self.get_directory_project()
        if len(customizedDirectory) > 1:
            name = customizedDirectory[len(customizedDirectory) - 1]
            customizedDirectory.pop()
            for word in customizedDirectory:
                relativePath = relativePath+"/"+word
            self.config['DIRECTORY_PROJECT'] = relativePath
        return name