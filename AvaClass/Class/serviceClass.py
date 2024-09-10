from AvaClass.helpers.CreateFile import create_file
from AvaClass.config.confReader import ConfEnv
from AvaClass.helpers.functions import firstLetterLowerCase
def create_service(conf:ConfEnv, nome_classe, nome_model, nome_repository, nome_dto):
    
    package = conf.get_package_code()
    postFix = conf.get_post_fix_service()
    directory = conf.get_package_services()

    directoryModel = conf.get_package_models()
    directoryRepository = conf.get_package_repositories()
    directoryDto = conf.get_package_dtos()

    nome_classe_completo = nome_classe + postFix
    nome_repository_letra_minuscula = firstLetterLowerCase(nome_repository)
    conteudo = f"""\
package {package}.{directory};

import {package}.{directoryDto}.{nome_dto};
import {package}.{directoryModel}.{nome_model};
import {package}.{directoryRepository}.{nome_repository};

import org.hibernate.ObjectNotFoundException;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.data.domain.Page;
import org.springframework.data.domain.Pageable;
import org.springframework.stereotype.Service;

import java.util.UUID;

@Service
public class {nome_classe_completo} {{
    private final {nome_repository} {nome_repository_letra_minuscula};

    @Autowired
    public {nome_classe_completo}({nome_repository} {nome_repository_letra_minuscula}) {{
        this.{nome_repository_letra_minuscula} = {nome_repository_letra_minuscula};
    }}

    public {nome_model} findById(UUID id) {{
        var model = {nome_repository_letra_minuscula}.findById(id);
        return model.orElseThrow(() -> new ObjectNotFoundException(id, {nome_model}.class.getName()));
    }}

    public {nome_dto} findByIdDTO(UUID id) {{
        var model = this.findById(id);
        return new {nome_dto}(model);
    }}

    public Page<{nome_dto}> findAll(Pageable pageable) {{
        Page<{nome_dto}> dtos = {nome_repository_letra_minuscula}.findAll(pageable).map((model) -> new {nome_dto}(model));
        return dtos;
    }}

    public {nome_dto} save({nome_dto} dto) {{
        var model = new {nome_model}(dto);
        {nome_repository_letra_minuscula}.save(model);
        return new {nome_dto}(model);
    }}

    public {nome_dto} update(UUID id, {nome_dto} dto) {{
        var model = this.findById(id);
        model.updateValues(dto);
        {nome_repository_letra_minuscula}.save(model);
        return new {nome_dto}(model);
    }}

    public void delete({nome_model} model) {{
        {nome_repository_letra_minuscula}.delete(model);
    }}
}}
"""
    # Verifica se o diretório existe, se não, cria
    create_file(conf.get_directory_project()+"/"+directory, nome_classe_completo, conteudo)