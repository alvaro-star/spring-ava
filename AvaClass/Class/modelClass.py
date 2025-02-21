from AvaClass.helpers.CreateFile import create_file
from AvaClass.config.confReader import ConfEnv


def create_model(confEnv: ConfEnv, nome_classe):
    # Verifica se o diretório existe, se não, cria
    package = confEnv.get_package_code()
    postFix = confEnv.get_post_fix_model()
    postFixDto = confEnv.get_post_fix_dto()
    directoryModel = confEnv.get_package_models()

    directoryDto = confEnv.get_package_dtos()
    nome_classe_completo = nome_classe + postFix
    nome_input_dto_completo = "Input" + nome_classe + postFixDto
    nome_output_dto_completo = "Output" + nome_classe + postFixDto
    conteudo = f"""\
package {package}.{directoryModel};

import {package}.{directoryDto}.{nome_input_dto_completo};
import {package}.{directoryDto}.{nome_output_dto_completo};
import jakarta.persistence.*;
import lombok.AllArgsConstructor;
import lombok.Data;
import lombok.NoArgsConstructor;
import org.hibernate.annotations.CreationTimestamp;
import org.hibernate.annotations.UpdateTimestamp;

import java.time.LocalDateTime;

@Data
@NoArgsConstructor
@AllArgsConstructor
@Entity
@SequenceGenerator(name = "seq_{nome_classe.lower()}", sequenceName = "seq_{nome_classe.lower()}", allocationSize = 1)
@Table(name = "tb_{nome_classe.lower()}")
public class {nome_classe_completo} {{
    @Id
    @GeneratedValue(strategy = GenerationType.SEQUENCE)
    @Column(name = "idtb_{nome_classe.lower()}")
    private Long id;
    
    private String nome;

    @CreationTimestamp
    @Column(name = "created_at", updatable = false, nullable = false)
    private LocalDateTime createdAt;

    @UpdateTimestamp
    @Column(name = "updated_at", nullable = false)
    private LocalDateTime updatedAt;
        
    public {nome_classe_completo}({nome_input_dto_completo} dto){{
    }}
    public void updateValues({nome_input_dto_completo} dto) {{
    }}
}}
"""

    conteudoInputDto = f"""\
package {package}.{directoryDto};

import {package}.{directoryModel}.{nome_classe_completo};

public record {nome_input_dto_completo}(
        Long id
) {{
    public {nome_input_dto_completo}({nome_classe_completo} model) {{
        this(model.getId());
    }}
}}

"""

    conteudoOutputDto = f"""\
package {package}.{directoryDto};

import {package}.{directoryModel}.{nome_classe_completo};

public record {nome_output_dto_completo}(
        Long id
) {{
    public {nome_output_dto_completo}({nome_classe_completo} model) {{
        this(model.getId());
    }}
}}

"""
    create_file(confEnv.get_directory_project() + "/" + directoryModel, nome_classe_completo, conteudo)
    create_file(confEnv.get_directory_project() + "/" + directoryDto, nome_input_dto_completo, conteudoInputDto)
    create_file(confEnv.get_directory_project() + "/" + directoryDto, nome_output_dto_completo, conteudoOutputDto)
