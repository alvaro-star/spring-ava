from AvaClass.helpers.CreateFile import create_file
from AvaClass.config.confReader import ConfEnv
from AvaClass.helpers.functions import firstLetterLowerCase


def create_resource(conf: ConfEnv, nome_classe: str, nome_dto, nome_service):
    postFix = conf.get_post_fix_resource()
    directoryResource = conf.get_package_resources()
    package = conf.get_package_code()
    directoryDto = conf.get_package_dtos()
    directoryService = conf.get_package_services()

    nome_resource_completo = nome_classe + postFix
    nome_service_letra_minuscula = firstLetterLowerCase(nome_service)

    nome_input_dto = "Input" + nome_dto
    nome_output_dto = "Output" + nome_dto

    conteudo = f"""\
package {package}.{directoryResource};

import {package}.{directoryDto}.{nome_input_dto};
import {package}.{directoryDto}.{nome_output_dto};
import {package}.{directoryService}.{nome_service};

import jakarta.validation.Valid;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.data.domain.Page;
import org.springframework.data.domain.Pageable;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

@RestController
@RequestMapping("/{nome_classe.lower() + 's'}")
public class {nome_resource_completo} {{
    @Autowired
    private {nome_service} {nome_service_letra_minuscula};

    @GetMapping("{{id}}")
    @ResponseStatus(HttpStatus.OK)
    public {nome_output_dto} findById(@PathVariable Long id) {{
        return {nome_service_letra_minuscula}.findByIdDTO(id);
    }}

    @GetMapping
    @ResponseStatus(HttpStatus.OK)
    public Page<{nome_output_dto}> findAll(Pageable pageable) {{
        return {nome_service_letra_minuscula}.findAll(pageable);
    }}

    @PostMapping
    @ResponseStatus(HttpStatus.CREATED)
    public {nome_output_dto} save(@RequestBody @Valid {nome_input_dto} dto) {{
        return {nome_service_letra_minuscula}.save(dto);
    }}

    @PutMapping("{{id}}")
    @ResponseStatus(HttpStatus.OK)
    public {nome_output_dto} update(@PathVariable Long id, @RequestBody @Valid {nome_input_dto} dto) {{
        return {nome_service_letra_minuscula}.update(id, dto);
    }}

    @DeleteMapping("{{id}}")
    @ResponseStatus(HttpStatus.NOT_CONTENT)
    public void delete(@PathVariable Long id) {{
        {nome_service_letra_minuscula}.delete(id);
    }}
}}
"""
    # Verifica se o diretório existe, se não, cria
    create_file(conf.get_directory_project() + "/" + directoryResource, nome_resource_completo, conteudo)
