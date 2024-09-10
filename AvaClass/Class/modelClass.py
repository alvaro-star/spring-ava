from AvaClass.helpers.CreateFile import create_file
from AvaClass.config.confReader import ConfEnv

def create_model(confEnv:ConfEnv, nome_classe):
    # Verifica se o diretório existe, se não, cria
    package = confEnv.get_package_code()
    postFix = confEnv.get_post_fix_model()
    postFixDto = confEnv.get_post_fix_dto()
    directoryModel = confEnv.get_package_models()

    directoryDto = confEnv.get_package_dtos()
    nome_classe_completo = nome_classe + postFix
    nome_dto_completo = nome_classe + postFixDto
    conteudo = f"""\
package {package}.{directoryModel};

import {package}.{directoryDto}.{nome_dto_completo};
import jakarta.persistence.*;
import lombok.AllArgsConstructor;
import lombok.Data;
import lombok.NoArgsConstructor;
import org.hibernate.annotations.CreationTimestamp;
import org.hibernate.annotations.UpdateTimestamp;

import java.time.LocalDateTime;
import java.util.UUID;

@Data
@NoArgsConstructor
@AllArgsConstructor
@Entity
@Table(name = "tb_{nome_classe.lower()}")
public class {nome_classe_completo} {{
    @Id
    @GeneratedValue(strategy = GenerationType.UUID)
    @Column(name = "idtb_{nome_classe.lower()}")
    private UUID id;
    
    private String nome;

    @CreationTimestamp
    @Column(name = "created_at", updatable = false, nullable = false)
    private LocalDateTime createdAt;

    @UpdateTimestamp
    @Column(name = "updated_at", nullable = false)
    private LocalDateTime updatedAt;
        
    public {nome_classe_completo}({nome_dto_completo} dto){{
    }}
    public void updateValues({nome_dto_completo} dto) {{
    }}
}}
"""
    
    conteudoDto = f"""\
package {package}.{directoryDto};

import {package}.{directoryModel}.{nome_classe_completo};

import java.util.UUID;

public record {nome_dto_completo}(
        UUID id
) {{
    public {nome_dto_completo}({nome_classe_completo} model) {{
        this(model.getId());
    }}
}}

"""
    create_file(confEnv.get_directory_project()+"/"+directoryModel, nome_classe_completo, conteudo)
    create_file(confEnv.get_directory_project()+"/"+directoryDto, nome_dto_completo, conteudoDto)