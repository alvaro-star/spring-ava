from AvaClass.helpers.CreateFile import create_file
from AvaClass.config.confReader import ConfEnv
def create_repository(conf:ConfEnv,nome_classe, nome_model):
    
    postFix = conf.get_post_fix_repository()
    directory = conf.get_package_repositories()
    package = conf.get_package_code()
    directoryModel = conf.get_package_models()

    nome_classe_completo = nome_classe + postFix

    conteudo = f"""\
package {package}.{directory};

import {package}.{directoryModel}.{nome_model};
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;

import java.util.UUID;

@Repository
public interface {nome_classe_completo} extends JpaRepository<{nome_model}, UUID> {{
}}
"""
    # Verifica se o diretório existe, se não, cria
    create_file(conf.get_directory_project()+"/"+ directory, nome_classe_completo, conteudo)