from AvaClass.helpers.CreateFile import create_file
from AvaClass.config.confReader import ConfEnv
from AvaClass.helpers.functions import firstLetterLowerCase

def create_resource(conf:ConfEnv,nome_classe, nome_dto, nome_service):
    
    postFix = conf.get_post_fix_resource()
    directoryResource =conf.get_package_resources()
    package = conf.get_package_code()
    directoryDto = conf.get_package_dtos()
    directoryService = conf.get_package_services()

    nome_resource_completo = nome_classe + postFix
    nome_service_letra_minuscula = firstLetterLowerCase(nome_service)
    conteudo = f"""\
package {package}.{directoryResource};

import {package}.{directoryDto}.{nome_dto};
import {package}.{directoryService}.{nome_service};

import jakarta.validation.Valid;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.data.domain.Page;
import org.springframework.data.domain.Pageable;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

import java.util.UUID;

@RestController
@RequestMapping("/pastas")
public class {nome_resource_completo} {{
    @Autowired
    private {nome_service} {nome_service_letra_minuscula};

    @GetMapping("/{{id}}")
    public ResponseEntity<{nome_dto}> getOne(@PathVariable("id") UUID id) {{
        var dto = {nome_service_letra_minuscula}.findByIdDTO(id);
        return ResponseEntity.ok(dto);
    }}

    @GetMapping
    public ResponseEntity<Page<{nome_dto}>> getAll(Pageable pageable) {{
        var dtos = {nome_service_letra_minuscula}.findAll(pageable);
        return ResponseEntity.ok(dtos);
    }}

    @PostMapping
    public ResponseEntity<{nome_dto}> save(@RequestBody @Valid {nome_dto} dto) {{
        var saved = {nome_service_letra_minuscula}.save(dto);
        return ResponseEntity.status(HttpStatus.CREATED).body(saved);
    }}

    @PutMapping("/{{id}}")
    public ResponseEntity<{nome_dto}> update(@PathVariable("id") UUID id, @RequestBody @Valid {nome_dto} dto) {{
        var updated = {nome_service_letra_minuscula}.update(id, dto);
        return ResponseEntity.ok(updated);
    }}

    @DeleteMapping("/{{id}}")
    public ResponseEntity<Object> delete(@PathVariable("id") UUID id) {{
        var model = {nome_service_letra_minuscula}.findById(id);
        {nome_service_letra_minuscula}.delete(model);
        return ResponseEntity.noContent().build();
    }}
}}
"""
    # Verifica se o diretório existe, se não, cria
    create_file(conf.get_directory_project()+"/"+directoryResource, nome_resource_completo, conteudo)