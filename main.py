import discord
import json
import requests
import os
from googletrans import Translator
from typing import Text
from discord.ext import commands

client = commands.Bot(command_prefix="/", case_insensitive=False)


@client.event
async def on_ready():
    activity = discord.Game(name='Artic idle', type=3)
    await client.change_presence(status=discord.Status.dnd, activity=activity)
    print("Conectando, por favor, aguarde...")


@client.event
async def on_message(message):
    if isinstance(message.channel, discord.DMChannel):
        return
    await client.process_commands(message)


@client.command()
async def clear(ctx, amount: int):
    await ctx.channel.purge(limit=amount)


@clear.error
async def clear_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArguments):
        await ctx.send('...')


#--------------------------------------------------------[𝐷𝐼𝑆𝑃𝑂𝑁𝐼́𝑉𝐸𝐼𝑆]-------------------------------------------------------#

@client.command() #𝐶𝑂𝑁𝑆𝑈𝐿𝑇𝐴𝑆 𝐷𝐼𝑆𝑃𝑂𝑁𝐼́𝑉𝐸𝐼𝑆
async def consulta(ctx):
    embed = discord.Embed(
        title='',
        description='',
        colour=16766976
    )

    embed.add_field(name="🕵🏻‍♂️ CONSULTA POR NOME",
                    value="Use o comando `/nome` {Nome Completo} para realizar a consulta.", inline=False)
    embed.add_field(name="👽 CONSULTA POR CPF",
                    value="Use o comando `/cpf` {CPF da Pessoa} para a consultar os dados.", inline=False)
    embed.add_field(name="📵 CONSULTA POR TELEFONE",
                    value="Use o comando `/telefone` {Telefone} para realizar a consulta.", inline=False)
    embed.add_field(name="🏨 CONSULTA DE CNPJ",
                    value="Use o comando `/cnpj` {CNPJ} para consultar os dados.", inline=False)
    embed.add_field(name="🚘 CONSULTA POR PLACA",
                    value="Use o comando `/placa` {Placa do veículo} para realizar a consulta.", inline=False)
    embed.add_field(name="📌 CONSULTA DE IP",
                    value="Use o comando `/ip` {IP} para realizar a consulta do IP.", inline=False)
    embed.add_field(name="💳 CONSULTA DE BIN",
                    value="Use o comando `/bin` {Número da BIN} para realizar a consulta.", inline=False)
    embed.add_field(name="📫 CONSULTA DE CEP",
                    value="Use o comando `/cep` {CEP da Rua} para realizar a consulta.", inline=False)
    embed.add_field(name="🦠 CONSULTA DE COVID19",
                    value="Use o comando `/covid` {Sigla do Estado} para realizar a consulta.", inline=False)
    embed.add_field(name="🏦 CONSULTA DE CÓDIGO BANCÁRIO",
                    value="Use o comando `/banco` {Código do Banco} para realizar a consulta.", inline=False)
    embed.add_field(name="💾 CONSULTA DE SITES",
                    value="Use o comando `/site` {URL do site} para realizar a consulta.", inline=False)
    embed.set_image(url='https://i.gifer.com/Cewn.gif')
    embed.set_author(name='Artic', icon_url='')
    embed.set_footer(text='Artic © All Rights Reserved', icon_url='https://i.imgur.com/KTXsLIQ.jpg')

    await ctx.send(embed=embed)

#--------------------------------------------------------[𝑁𝑂𝑀𝐸]-------------------------------------------------------#

@client.command() #𝐶𝑂𝑁𝑆𝑈𝐿𝑇𝐴 𝐷𝐸 𝑁𝑂𝑀𝐸
async def nome(ctx):
    embed = discord.Embed(
        title='',
        description='A Consulta por ***NOME*** estará disponível em breve. No momento,\nestamos com ***ausência*** das APIs de consultas por ***nome***!',
        colour=16737991
    )

    embed.set_author(name='ㅤㅤㅤㅤㅤㅤㅤㅤCONSULTA DE NOMEㅤㅤㅤㅤㅤㅤㅤㅤ', icon_url='')

    embed.set_footer(text='Requested By {}'.format(ctx.author), icon_url=ctx.author.avatar_url)

    await ctx.send(embed=embed)

#--------------------------------------------------------[𝐶𝑃𝐹]---------------------------------------------------------#

@client.command() #𝐶𝑂𝑁𝑆𝑈𝐿𝑇𝐴 𝐷𝐸 𝐶𝑃𝐹
async def cpf(ctx):
    embed = discord.Embed(
        title='',
        description='A Consulta por ***CPF*** estará disponível em breve. No momento,\nestamos com ***ausência*** das APIs de consultas por ***CPF!***',
        colour=16745472
    )

    embed.add_field(name="➢ CPF", value='SEM INFORMAÇÃO', inline=False)
    embed.add_field(name="➢ CNS", value='SEM INFORMAÇÃO', inline=False)
    embed.add_field(name="➢ RG", value='SEM INFORMAÇÃO', inline=False)
    embed.add_field(name="➢ DATA DE EXPEDIÇÃO", value='SEM INFORMAÇÃO', inline=False)
    embed.add_field(name="➢ UF - RG", value='SEM INFORMAÇÃO', inline=False)
    embed.add_field(name="➢ TÍTULO ELEITORAL", value='SEM INFORMAÇÃO', inline=False)
    embed.add_field(name="➢ NOME", value='SEM INFORMAÇÃO', inline=False)
    embed.add_field(name="➢ NASCIMENTO", value='SEM INFORMAÇÃO', inline=False)
    embed.add_field(name="➢ IDADE", value='SEM INFORMAÇÃO', inline=False)
    embed.add_field(name="➢ SIGNO", value='SEM INFORMAÇÃO', inline=False)
    embed.add_field(name="➢ SEXO", value='SEM INFORMAÇÃO', inline=False)
    embed.add_field(name="➢ COR", value='SEM INFORMAÇÃO', inline=False)
    embed.add_field(name="➢ TIPO SANGUÍNEO", value='SEM INFORMAÇÃO', inline=False)
    embed.add_field(name="➢ MÃE", value='SEM INFORMAÇÃO', inline=False)
    embed.add_field(name="➢ PAI", value='SEM INFORMAÇÃO', inline=False)
    embed.add_field(name="➢ PAÍS DE NASCIMENTO", value='SEM INFORMAÇÃO', inline=False)
    embed.add_field(name="➢ CIDADE DE NASCIMENTO", value='SEM INFORMAÇÃO', inline=False)
    embed.add_field(name="➢ ESTADO DE NASCIMENTO", value='SEM INFORMAÇÃO', inline=False)
    embed.add_field(name="➢ LOGRADOURO", value='SEM INFORMAÇÃO', inline=False)
    embed.add_field(name="➢ NÚMERO", value='SEM INFORMAÇÃO', inline=False)
    embed.add_field(name="➢ COMPLEMENTO", value='SEM INFORMAÇÃO', inline=False)
    embed.add_field(name="➢ BAIRRO", value='SEM INFORMAÇÃO', inline=False)
    embed.add_field(name="➢ CIDADE", value='SEM INFORMAÇÃO', inline=False)
    embed.add_field(name="➢ ESTADO", value='SEM INFORMAÇÃO', inline=False)
    embed.add_field(name="➢ PAÍS", value='SEM INFORMAÇÃO', inline=False)
    embed.add_field(name="➢ CEP", value='SEM INFORMAÇÃO', inline=False)
    embed.add_field(name="➢ E-MAIL", value='SEM INFORMAÇÃO', inline=False)
    embed.add_field(name="➢ TELEFONE", value='SEM INFORMAÇÃO', inline=False)

    embed.set_author(name='ㅤㅤㅤㅤㅤㅤㅤㅤCONSULTA DE CPFㅤㅤㅤㅤㅤㅤㅤㅤ', icon_url='')

    embed.set_footer(text='Requested By {}'.format(ctx.author), icon_url=ctx.author.avatar_url)

    await ctx.send(embed=embed)

#--------------------------------------------------------[𝑇𝐸𝐿𝐸𝐹𝑂𝑁𝐸]-------------------------------------------------------------#

@client.command() #𝐶𝑂𝑁𝑆𝑈𝐿𝑇𝐴 𝐷𝐸 𝑇𝐸𝐿𝐸𝐹𝑂𝑁𝐸
async def telefone(ctx):
    embed = discord.Embed(
        title='',
        description='A Consulta por ***TELEFONE*** estará disponível em breve. No momento,\nestamos com ***ausência*** das APIs de consultas por ***telefone!***',
        colour=6084221
    )

    embed.add_field(name="➢ TELEFONE", value='SEM INFORMAÇÃO', inline=False)
    embed.add_field(name="➢ NOME", value='SEM INFORMAÇÃO', inline=False)
    embed.add_field(name="➢ CPF/CNPJ", value='SEM INFORMAÇÃO', inline=False)
    embed.add_field(name="➢ LOGRADOURO", value='SEM INFORMAÇÃO', inline=False)
    embed.add_field(name="➢ NÚMERO", value='SEM INFORMAÇÃO', inline=False)
    embed.add_field(name="➢ COMPLEMENTO", value='SEM INFORMAÇÃO', inline=False)
    embed.add_field(name="➢ BAIRRO", value='SEM INFORMAÇÃO', inline=False)
    embed.add_field(name="➢ CIDADE", value='SEM INFORMAÇÃO', inline=False)
    embed.add_field(name="➢ ESTADO", value='SEM INFORMAÇÃO', inline=False)
    embed.add_field(name="➢ CEP", value='SEM INFORMAÇÃO', inline=False)

    embed.set_author(name='ㅤㅤㅤㅤㅤㅤㅤㅤCONSULTA DE TELEFONEㅤㅤㅤㅤㅤㅤㅤㅤ', icon_url='')

    embed.set_footer(text='Requested By {}'.format(ctx.author), icon_url=ctx.author.avatar_url)

    await ctx.send(embed=embed)

#--------------------------------------------------------[𝑃𝐿𝐴𝐶𝐴]-------------------------------------------------------------#

@client.command() #𝐶𝑂𝑁𝑆𝑈𝐿𝑇𝐴 𝐷𝐸 𝑃𝐿𝐴𝐶𝐴
async def placa(ctx):
    embed = discord.Embed(
        title='',
        description='A Consulta por ***PLACA*** estará disponível em breve. No momento,\nestamos com ***ausência*** das APIs de consultas por ***placa!***',
        colour=6646071
    )

    embed.add_field(name="➢ PLACA", value='SEM INFORMAÇÃO', inline=False)
    embed.add_field(name="➢ SITUAÇÃO", value='SEM INFORMAÇÃO', inline=False)
    embed.add_field(name="➢ MARCA", value='SEM INFORMAÇÃO', inline=False)
    embed.add_field(name="➢ MODELO", value='SEM INFORMAÇÃO', inline=False)
    embed.add_field(name="➢ COR", value='SEM INFORMAÇÃO', inline=False)
    embed.add_field(name="➢ ANO - FABRICAÇÃO.", value='SEM INFORMAÇÃO', inline=False)
    embed.add_field(name="➢ ANO - MODELO", value='SEM INFORMAÇÃO', inline=False)
    embed.add_field(name="➢ MUNICIPIO", value='SEM INFORMAÇÃO', inline=False)
    embed.add_field(name="➢ ESTADO", value='SEM INFORMAÇÃO', inline=False)
    embed.add_field(name="➢ CHASSI", value='SEM INFORMAÇÃO', inline=False)
    embed.add_field(name="➢ RENAVAM", value='SEM INFORMAÇÃO', inline=False)
    embed.add_field(name="➢ FATURADO", value='SEM INFORMAÇÃO', inline=False)
    embed.add_field(name="➢ UF - FATURADO", value='SEM INFORMAÇÃO', inline=False)
    embed.add_field(name="➢ MUNICÍPIO - FABRICAÇÃO.", value='SEM INFORMAÇÃO', inline=False)
    embed.add_field(name="➢ ESTADO - FABRICAÇÃO", value='SEM INFORMAÇÃO', inline=False)
    embed.add_field(name="➢ SEGMENTO", value='SEM INFORMAÇÃO', inline=False)
    embed.add_field(name="➢ SUB SEGMENTO", value='SEM INFORMAÇÃO', inline=False)
    embed.add_field(name="➢ GRUPO", value='SEM INFORMAÇÃO', inline=False)
    embed.add_field(name="➢ COMBUSTÍVEL", value='SEM INFORMAÇÃO', inline=False)
    embed.add_field(name="➢ POTÊNCIA", value='SEM INFORMAÇÃO', inline=False)
    embed.add_field(name="➢ CILINDRADAS", value='SEM INFORMAÇÃO', inline=False)
    embed.add_field(name="➢ CAPACIDADE DE CARGA", value='SEM INFORMAÇÃO', inline=False)
    embed.add_field(name="➢ NACIONALIDADE", value='SEM INFORMAÇÃO', inline=False)
    embed.add_field(name="➢ LINHA", value='SEM INFORMAÇÃO', inline=False)
    embed.add_field(name="➢ CARROCERIA", value='SEM INFORMAÇÃO', inline=False)
    embed.add_field(name="➢ EIXO TRASEIRO", value='SEM INFORMAÇÃO', inline=False)
    embed.add_field(name="➢ MOTOR", value='SEM INFORMAÇÃO', inline=False)
    embed.add_field(name="➢ TIPO DE PESSOA", value='SEM INFORMAÇÃO', inline=False)
    embed.add_field(name="➢ TIPO DE VEÍCULO", value='SEM INFORMAÇÃO', inline=False)
    embed.add_field(name="➢ QUANTIDADE DE PASSAGEIROS", value='SEM INFORMAÇÃO', inline=False)
    embed.add_field(name="➢ ID IMPORTADORA", value='SEM INFORMAÇÃO', inline=False)
    embed.add_field(name="➢ DI", value='SEM INFORMAÇÃO', inline=False)
    embed.add_field(name="➢ REGISTRO DI", value='SEM INFORMAÇÃO', inline=False)
    embed.add_field(name="➢ UNIDADE LOCAL SRF", value='SEM INFORMAÇÃO', inline=False)
    embed.add_field(name="➢ ÚLTIMA ATUALIZAÇÃO", value='SEM INFORMAÇÃO', inline=False)
    embed.add_field(name="➢ NOME DO PROPRIETÁRIO", value='SEM INFORMAÇÃO', inline=False)
    embed.add_field(name="➢ CPF/CNPJ DO PROPRIETÁRIO", value='SEM INFORMAÇÃO', inline=False)
    embed.add_field(name="➢ PLACA MODELO ANTIGO", value='SEM INFORMAÇÃO', inline=False)
    embed.add_field(name="➢ PLACA MODELO NOVO", value='SEM INFORMAÇÃO', inline=False)

    embed.set_author(name='ㅤㅤㅤㅤㅤㅤㅤㅤCONSULTA DE PLACAㅤㅤㅤㅤㅤㅤㅤㅤ', icon_url='')

    embed.set_footer(text='Requested By {}'.format(ctx.author), icon_url=ctx.author.avatar_url)

    await ctx.send(embed=embed)

#--------------------------------------------------------[𝐶𝑁𝑃𝐽]-------------------------------------------------------------#

@client.command() #𝐶𝑂𝑁𝑆𝑈𝐿𝑇𝐴 𝐷𝐸 𝐶𝑁𝑃𝐽
async def cnpj(ctx, cnpj = 0):
    data = requests.get(f"https://brasilapi.com.br/api/cnpj/v1/{cnpj}").json()


    try:
        embed = discord.Embed(
            title='',
            colour=8978176
        )
        
        validateCnpj = data["cnpj"] if data["cnpj"] != "" else "Não encontrado"
        validateNome = data["nome_fantasia"] if data["nome_fantasia"] != "" else "Não encontrado"
        validateRazao = data["razao_social"] if data["razao_social"] != "" else "Não encontrado"
        validateStatus = data["descricao_situacao_cadastral"] if data["descricao_situacao_cadastral"] != "" else "Não encontrado"
        validateUf = data["uf"] if data["uf"] != "" else "Não encontrado"
        validateComplemento = data["complemento"] if data["complemento"] != "" else "Não encontrado"
        validateBairro = data["bairro"] if data["bairro"] != "" else "Não encontrado"
        validateNumero = data["numero"] if data["numero"] != "" else "Não encontrado"
        validateMunicipio = data["municipio"] if data["municipio"] != "" else "Não encontrado"
        validateData = data["data_inicio_atividade"] if data["data_inicio_atividade"] != "" else "Não encontrado"
        validateCnae = data["cnae_fiscal_descricao"] if data["cnae_fiscal_descricao"] != "" else "Não encontrado"
        validateCnaeCod = data["cnae_fiscal"] if data["cnae_fiscal"] != "" else "Não encontrado"
        validateMatriz = data["identificador_matriz_filial"] if data["identificador_matriz_filial"] != "" else "Não encontrado"
        validateFilial = data["descricao_matriz_filial"] if data["descricao_matriz_filial"] != "" else "Não encontrado"
        validateDataSituacao = data["data_situacao_cadastral"] if data["data_situacao_cadastral"] != "" else "Não encontrado"
        validateJuridica = data["codigo_natureza_juridica"] if data["codigo_natureza_juridica"] != "" else "Não encontrado"
        validateLogradouro = data["logradouro"] if data["logradouro"] != "" else "Não encontrado"
        validateTelefone1 = data["ddd_telefone_1"] if data["ddd_telefone_1"] != "" else "Não encontrado"
        validateTelefone2 = data["ddd_telefone_2"] if data["ddd_telefone_2"] != "" else "Não encontrado"
        validateQualificacao = data["qualificacao_do_responsavel"] if data["qualificacao_do_responsavel"] != "" else "Não encontrado"
        validateCapital = data["capital_social"] if data["capital_social"] != "" else "Não encontrado"
        validateDescricaoPorte = data["descricao_porte"] if data["descricao_porte"] != "" else "Não encontrado"
        validateSimples = data["opcao_pelo_simples"] if data["opcao_pelo_simples"] != "" else "Não encontrado"
        validateSimplesDate = data["data_opcao_pelo_simples"] if data["data_opcao_pelo_simples"] != "" else "Não encontrado"
        validateCep = data["cep"] if data["cep"] != "" else "Não encontrado"
        

        embed.add_field(name="➢ CNPJ", value=validateCnpj, inline=False)
        embed.add_field(name="➢ NOME FANTASIA", value=validateNome, inline=False)
        embed.add_field(name="➢ RAZÃO SOCIAL", value=validateRazao, inline=False)
        embed.add_field(name="➢ MATRIZ FILIAL", value=validateMatriz, inline=False)
        embed.add_field(name="➢ DESCRIÇÃO MATRIZ", value=validateFilial, inline=False)
        embed.add_field(name="➢ DATA SITUAÇÃO CADASTRAL", value=validateDataSituacao, inline=False)
        embed.add_field(name="➢ NATUREZA JURÍDICA", value=validateJuridica, inline=False)
        embed.add_field(name="➢ QUALIFICAÇÃO DO RESPONSÁVEL", value=validateQualificacao, inline=False)
        embed.add_field(name="➢ CAPITAL SOCIAL", value=validateCapital, inline=False)
        embed.add_field(name="➢ DESCRIÇÃO DO PORTE", value=validateDescricaoPorte, inline=False)
        embed.add_field(name="➢ OPÇÃO PELO SIMPLES", value=validateSimples, inline=False)
        embed.add_field(name="➢ DATA OPÇÃO PELO SIMPLES", value=validateSimplesDate, inline=False)
        embed.add_field(name="➢ STATUS", value=validateStatus, inline=False)
        embed.add_field(name="➢ LOGRADOURO", value=validateLogradouro, inline=False)
        embed.add_field(name="➢ NÚMERO", value=validateNumero, inline=False)
        embed.add_field(name="➢ MUNICÍPIO", value=validateMunicipio, inline=False)
        embed.add_field(name="➢ BAIRRO", value=validateBairro, inline=False)
        embed.add_field(name="➢ COMPLEMENTO", value=validateComplemento, inline=False)
        embed.add_field(name="➢ CEP", value=validateCep, inline=False)
        embed.add_field(name="➢ UF - Unidade Federativa", value=validateUf, inline=False)
        embed.add_field(name="➢ TELEFONE 1", value=validateTelefone1, inline=False)
        embed.add_field(name="➢ TELEFONE 2", value=validateTelefone2, inline=False)
        embed.add_field(name="➢ DATA DE ABERTURA", value=validateData, inline=False)
        embed.add_field(name="➢ CNAE", value=validateCnae, inline=False)
        embed.add_field(name="➢ CNAE FISCAL", value=validateCnaeCod, inline=False)

        embed.set_author(name='ㅤㅤㅤㅤㅤㅤㅤㅤCONSULTA DE CNPJㅤㅤㅤㅤㅤㅤㅤㅤ', icon_url='')
    
        embed.set_footer(text='Requested By {}'.format(ctx.author), icon_url=ctx.author.avatar_url)

        await ctx.send(embed=embed)
    
        return
    except Exception:
        pass

    error = data["message"]
    embed = discord.Embed(
        title='',
        colour=16766976
    )
        
    embed.add_field(name="Use `/cnpj` {cnpj} ", value='Exemplo: /cnpj 12345678901234', inline=False)

    embed.set_author(name='⚠️ CNPJ NÃO ENCONTRADO ⚠️', icon_url='')

    await ctx.send(embed=embed)
        

#--------------------------------------------------------[𝐼𝑃]-------------------------------------------------------------#

@client.command() #𝐶𝑂𝑁𝑆𝑈𝐿𝑇𝐴 𝐷𝐸 𝐼𝑃
async def ip(ctx, ip):
    data = requests.get(f"http://ipwhois.app/json/{ip}").json()
    
    try:
        error = data["message"]
        embed = discord.Embed(
            title='⚠️ IP NÃO ENCONTRADO ⚠️',
            description='',
            colour=16766976
        )

        embed.set_author(name='', icon_url='')

        await ctx.send(embed=embed)

        return
    except Exception:
        pass

        embed = discord.Embed(
            title='',
            colour=16777215
        )

        validateAsn = data["asn"] if data["asn"] != "" else "Não encontrado"

    embed.add_field(name="➢ IP", value=data['ip'], inline=False)
    embed.add_field(name="➢ CIDADE", value=data['city'], inline=False)
    embed.add_field(name="➢ ESTADO", value=data['region'], inline=False)
    embed.add_field(name="➢ PAÍS", value=data['country'], inline=False)
    embed.add_field(name="➢ CONTINENTE", value=data["continent"], inline=False)
    embed.add_field(name="➢ LATITUDE", value=data['latitude'], inline=False)
    embed.add_field(name="➢ LONGITUDE", value=data['longitude'], inline=False)
    embed.add_field(name="➢ PROVEDOR", value=data['isp'], inline=False)
    embed.add_field(name="➢ ASN", value=validateAsn, inline=False)
    embed.add_field(name="➢ EMPRESA RESPONSÁVEL", value=data['org'], inline=False)
    embed.add_field(name="➢ TIPO DE CONEXÃO", value=data['type'], inline=False)

    embed.set_author(name='ㅤㅤㅤㅤㅤㅤㅤㅤCONSULTA DE IPㅤㅤㅤㅤㅤㅤㅤㅤ', icon_url='')

    embed.set_footer(text='Requested By {}'.format(ctx.author), icon_url=ctx.author.avatar_url)

    await ctx.send(embed=embed)

#--------------------------------------------------------[𝐶𝑂𝑉𝐼𝐷19]-------------------------------------------------------------#

@client.command() #𝐶𝑂𝑁𝑆𝑈𝐿𝑇𝐴 𝐷𝐸 𝐶𝑂𝑉𝐼𝐷19
async def covid(ctx, covid):
    data = requests.get(f"https://covid19-brazil-api.vercel.app/api/report/v1/brazil/uf/{covid}").json()

    try:
        error = data["error"]
        embed = discord.Embed(
            title='⚠️ ESTADO NÃO ENCONTRADO ⚠️',
            colour=16766976
        )

        embed.set_author(name='', icon_url='')

        await ctx.send(embed=embed)

        return
    except Exception:
        pass

        embed = discord.Embed(
            title='',
            colour=13841202
        )

    embed.add_field(name="➢ ESTADO", value=data['state'], inline=False)
    embed.add_field(name="➢ CASOS", value=data['cases'], inline=False)
    embed.add_field(name="➢ MORTES", value=data['deaths'], inline=False)
    embed.add_field(name="➢ SUSPEITOS", value=data['suspects'], inline=False)
    embed.add_field(name="➢ DESCARTADOS", value=data['refuses'], inline=False)
    embed.add_field(name="➢ DATA DE ATUALIZAÇÃO", value=data['datetime'], inline=False)

    embed.set_author(name='ㅤㅤㅤㅤㅤㅤㅤㅤCONSULTA DE COVID19ㅤㅤㅤㅤㅤㅤㅤㅤ', icon_url='')

    embed.set_footer(text='Requested By {}'.format(ctx.author), icon_url=ctx.author.avatar_url)

    await ctx.send(embed=embed)

#--------------------------------------------------------[𝐶𝐸𝑃]-------------------------------------------------------------#

@client.command() #𝐶𝑂𝑁𝑆𝑈𝐿𝑇𝐴 𝐷𝐸 𝐶𝐸𝑃
async def cep(ctx, cep):
    data = requests.get(f"https://cep.awesomeapi.com.br/json/{cep}").json()

    try:
        error = data["message"]
        embed = discord.Embed(
            title='⚠️ CEP NÃO ENCONTRADO ⚠️',
            colour=16766976
        )

        await ctx.send(embed=embed)

        return
    except Exception:
        pass

        embed = discord.Embed(
            title='',
            colour=16766208
        )

    embed.add_field(name="➢ CEP", value=data['cep'], inline=False)
    embed.add_field(name="➢ RUA", value=data['address'], inline=False)
    embed.add_field(name="➢ BAIRRO", value=data['district'], inline=False)
    embed.add_field(name="➢ CIDADE", value=data['city'], inline=False)
    embed.add_field(name="➢ ESTADO", value=data['state'], inline=False)
    embed.add_field(name="➢ LOGRADOURO", value=data['address_name'], inline=False)
    embed.add_field(name="➢ LATITUDE", value=data['lat'], inline=False)
    embed.add_field(name="➢ LONGITUDE", value=data['lng'], inline=False)
    embed.add_field(name="➢ IBGE", value=data['city_ibge'], inline=False)
    embed.add_field(name="➢ DDD", value=data['ddd'], inline=False)

    embed.set_author(name='ㅤㅤㅤㅤㅤㅤㅤㅤCONSULTA DE CEPㅤㅤㅤㅤㅤㅤㅤㅤ', icon_url='')

    embed.set_footer(text='Requested By {}'.format(ctx.author), icon_url=ctx.author.avatar_url)

    await ctx.send(embed=embed)

#--------------------------------------------------------[𝐵𝐴𝑁𝐶𝐴́𝑅𝐼𝑂]-------------------------------------------------------------#

@client.command() #𝐶𝑂𝑁𝑆𝑈𝐿𝑇𝐴 𝐶𝑂́𝐷𝐼𝐺𝑂 𝐵𝐴𝑁𝐶𝐴́𝑅𝐼𝑂
async def banco(ctx, banco):
    data = requests.get(f"https://brasilapi.com.br/api/banks/v1/{banco}").json()

    try:
        error = data["message"]
        embed = discord.Embed(
            title='⚠️ CÓDIGO BANCÁRIO NÃO ENCONTRADO ⚠️',
            description='',
            colour=16766976
        )

        embed.set_author(name='', icon_url='')

        await ctx.send(embed=embed)

        return
    except Exception:
        pass

        embed = discord.Embed(
            title='',
            colour=7667888
        )

    embed.add_field(name="➢ ISPB", value=data['ispb'], inline=False)
    embed.add_field(name="➢ NOME DO BANCO", value=data['name'], inline=False)
    embed.add_field(name="➢ CÓDIGO BANCÁRIO", value=data['code'], inline=False)
    embed.add_field(name="➢ INFORMAÇÕES ADICIONAIS", value=data['fullName'], inline=False)

    embed.set_author(name='ㅤㅤㅤㅤㅤㅤㅤㅤCONSULTA DE BANCOㅤㅤㅤㅤㅤㅤㅤㅤ', icon_url='')

    embed.set_footer(text='Requested By {}'.format(ctx.author), icon_url=ctx.author.avatar_url)

    await ctx.send(embed=embed)

#--------------------------------------------------------[𝐵𝐼𝑁]-------------------------------------------------------------#

@client.command() #𝐶𝑂𝑁𝑆𝑈𝐿𝑇𝐴 𝐷𝐸 𝐵𝐼𝑁
async def bin(ctx, bin):
    data = requests.get(
        f"https://api.bincodes.com/bin/?format=json&api_key=c0107d14acda7e1831dfe26ee8e8b3a5&bin={bin}").json()

    try:
        error = data["message"]
        embed = discord.Embed(
            title='⚠️ BIN NÃO ENCONTRADO ⚠️',
            colour=16766976
        )

        await ctx.send(embed=embed)

        return
    except Exception:
        pass

        embed = discord.Embed(
            title='',
            colour=16711701
        )

    embed.add_field(name="➢ BIN", value=data['bin'], inline=False)
    embed.add_field(name="➢ MODELO", value=data['type'], inline=False)
    embed.add_field(name="➢ NÍVEL", value=data['level'], inline=False)
    embed.add_field(name="➢ BANDEIRA", value=data['card'], inline=False)
    embed.add_field(name="➢ PAÍS", value=data['country'], inline=False)
    embed.add_field(name="➢ SIGLA", value=data['countrycode'], inline=False)
    embed.add_field(name="➢ BANCO", value=data['bank'], inline=False)

    embed.set_author(name='ㅤㅤㅤㅤㅤㅤㅤㅤCONSULTA DE BINㅤㅤㅤㅤㅤㅤㅤㅤ', icon_url='')

    embed.set_footer(text='Requested By {}'.format(ctx.author), icon_url=ctx.author.avatar_url)

    await ctx.send(embed=embed)

#--------------------------------------------------------[𝑆𝐼𝑇𝐸]-------------------------------------------------------------#

@client.command() #𝐶𝑂𝑁𝑆𝑈𝐿𝑇𝐴 𝐷𝐸 𝑆𝐼𝑇𝐸
async def site(ctx, site):
    data = requests.get(f"http://ipwhois.app/json/{site}").json()

    try:
        error = data["message"]
        embed = discord.Embed(
            title='⚠️ SITE NÃO ENCONTRADO ⚠️',
            description='',
            colour=16766976
        )

        embed.set_author(name='', icon_url='')

        await ctx.send(embed=embed)

        return
    except Exception:
        pass

        embed = discord.Embed(
            title='',
            colour=58879
        )

    embed.add_field(name="➢ IP", value=data['ip'], inline=False)
    embed.add_field(name="➢ CIDADE", value=data['city'], inline=False)
    embed.add_field(name="➢ ESTADO", value=data['region'], inline=False)
    embed.add_field(name="➢ PAÍS", value=data['country'], inline=False)
    embed.add_field(name="➢ LATITUDE", value=data['latitude'], inline=False)
    embed.add_field(name="➢ LONGITUDE", value=data['longitude'], inline=False)
    embed.add_field(name="➢ ORGANIZAÇÃO", value=data['isp'], inline=False)
    embed.add_field(name="➢ EMPRESA", value=data['org'], inline=False)
    embed.add_field(name="➢ FUSO HORÁRIO", value=data['timezone'], inline=False)

    embed.set_author(name='ㅤㅤㅤㅤㅤㅤㅤㅤCONSULTA DE SITEㅤㅤㅤㅤㅤㅤㅤㅤ', icon_url='')

    embed.set_footer(text='Requested By {}'.format(ctx.author), icon_url=ctx.author.avatar_url)

    await ctx.send(embed=embed)

#--------------------------------------------------------[𝑂𝑃𝐸𝑅𝐴𝐷𝑂𝑅𝐴]-------------------------------------------------------------#

@client.command() #𝐶𝑂𝑁𝑆𝑈𝐿𝑇𝐴 𝐷𝐸 𝑂𝑃𝐸𝑅𝐴𝐷𝑂𝑅𝐴
async def operadora(ctx, operadora):
    data = requests.get(f"http://apilayer.net/api/validate?access_key=317fca6d1dc194d6c5e5d16898b63ddf&number={operadora}&country_code=&format=1").json()

    try:
        error = data["error"]
        embed = discord.Embed(
            title='⚠️ FORMATO INVÁLIDO! ⚠️',
            description='',
            colour=16766976
        )

        embed.set_author(name='', icon_url='')

        await ctx.send(embed=embed)

        return
    except Exception:
        pass

        embed = discord.Embed(
            title='',
            colour=16711927
        )

    embed.add_field(name="➢ VÁLIDO", value=data['valid'], inline=False)
    embed.add_field(name="➢ NÚMERO", value=data['number'], inline=False)
    embed.add_field(name="➢ FORMATO INTERNACIONAL", value=data['international_format'], inline=False)
    embed.add_field(name="➢ DDI DO PAÍS", value=data['country_prefix'], inline=False)
    embed.add_field(name="➢ CÓDIGO DO PAÍS", value=data['country_code'], inline=False)
    embed.add_field(name="➢ NOME DO PAÍS", value=data['country_name'], inline=False)
    embed.add_field(name="➢ LOCALIZAÇÃO", value=data['location'], inline=False)
    embed.add_field(name="➢ OPERADORA/PROVEDOR", value=data['carrier'], inline=False)
    embed.add_field(name="➢ LINHA DE DISPOSITÍVO", value=data['line_type'], inline=False)

    embed.set_author(name='ㅤㅤㅤㅤㅤㅤㅤㅤCONSULTA DE OPERADORAㅤㅤㅤㅤㅤㅤㅤㅤ', icon_url='')

    embed.set_footer(text='Requested By {}'.format(ctx.author), icon_url=ctx.author.avatar_url)

    await ctx.send(embed=embed)

#--------------------------------------------------------[𝑀𝑂𝐸𝐷𝐴𝑆]-------------------------------------------------------------#

@client.command() #𝐶𝑂𝑇𝐴𝐶̧𝐴̃𝑂 𝐷𝐸 𝑀𝑂𝐸𝐷𝐴𝑆
async def cotacao(ctx, cotacao):
    data = requests.get(f"https://economia.awesomeapi.com.br/last/{cotacao}").json()
    coin_name = cotacao.replace("-", "")

    try:
        error = data["message"]
        embed = discord.Embed(
            title='⚠️ MOEDA NÃO ENCONTRADA ⚠️',
            description='',
            colour=16766976
        )

        
        embed.set_author(name='', icon_url='')

        await ctx.send(embed=embed)

        return
    except Exception:
        pass

        embed = discord.Embed(
            title='',
            colour=3560703
        )
    
    embed.add_field(name="➢ MOEDA A COMPARAR", value=data[coin_name]["code"], inline=False)
    embed.add_field(name="➢ MOEDA A SER COMPARADA", value=data[coin_name]["codein"], inline=False)
    embed.add_field(name="➢ NOME DAS PARIEDADES", value=data[coin_name]["name"], inline=False)
    embed.add_field(name="➢ MÁXIMA DO DIA", value=data[coin_name]["high"], inline=False)
    embed.add_field(name="➢ MÍNIMA DO DIA", value=data[coin_name]["low"], inline=False)
    embed.add_field(name="➢ VARIAÇÃO", value=data[coin_name]["varBid"], inline=False)
    embed.add_field(name="➢ PORCENTAGEM DE VARIAÇÃO", value=data[coin_name]["pctChange"], inline=False)
    embed.add_field(name="➢ COMPRA", value=data[coin_name]["bid"], inline=False)
    embed.add_field(name="➢ VENDA", value=data[coin_name]["ask"], inline=False)
    embed.add_field(name="➢ ATUALIZAÇÃO", value=data[coin_name]["create_date"], inline=False)

    embed.set_author(name='ㅤㅤㅤㅤㅤㅤㅤㅤCOTAÇÃO DE MOEDASㅤㅤㅤㅤㅤㅤㅤㅤ', icon_url='')

    embed.set_footer(text='Requested By {}'.format(ctx.author), icon_url=ctx.author.avatar_url)

    await ctx.send(embed=embed)

#--------------------------------------------------------[𝐷𝐷𝐷]-------------------------------------------------------------#

@client.command() #𝐶𝑂𝑁𝑆𝑈𝐿𝑇𝐴 𝐷𝐸 𝐶𝐼𝐷𝐴𝐷𝐸𝑆 𝑃𝑂𝑅 𝐷𝐷𝐷
async def ddd(ctx, ddd):
    data = requests.get(f"https://brasilapi.com.br/api/ddd/v1/{ddd}").json()

    try:
        error = data["message"]
        embed = discord.Embed(
            title='⚠️ CIDADE INVÁLIDA ⚠️',
            description='',
            colour=16766976
        )

        embed.set_author(name='', icon_url='')

        await ctx.send(embed=embed)

        return
    except Exception:
        pass

        embed = discord.Embed(
            title='',
            colour=58879
        )

    embed.add_field(name="➢ ESTADO", value=data['state'], inline=False)
    embed.add_field(name="➢ CIDADES", value='\n'.join([f"{city}" for city in data["cities"]]), inline=False)
    embed.set_author(name='ㅤㅤㅤㅤㅤㅤㅤㅤCONSULTA DE CIDADES POR DDDㅤㅤㅤㅤㅤㅤㅤㅤ', icon_url='')

    embed.set_footer(text='Requested By {}'.format(ctx.author), icon_url=ctx.author.avatar_url)

    await ctx.send(embed=embed)

#--------------------------------------------------------[𝐹𝐸𝑅𝐼𝐴𝐷𝑂𝑆]-------------------------------------------------------------#

@client.command() #𝐶𝑂𝑁𝑆𝑈𝐿𝑇𝐴 𝐷𝐸 𝐹𝐸𝑅𝐼𝐴𝐷𝑂𝑆
async def feriados(ctx, feriados):
    data = requests.get(f"https://brasilapi.com.br/api/feriados/v1/{feriados}").json()

    try:
        error = data["message"]
        embed = discord.Embed(
            title='⚠️ ANO INVÁLIDO (SUPORTADO SOMENTE DE 1900 À 2199) ⚠️',
            description='',
            colour=16766976
        )

        embed.set_author(name='', icon_url='')

        await ctx.send(embed=embed)

        return
    except Exception:
        pass

        embed = discord.Embed(
            title='',
            colour=58879
        )

    embed.add_field(name="➢ FERIADOS", value='\n\n'.join([f"{holiday['name'].upper() + ' ★ ' + holiday['date'].replace('-', '/') + ' ★ ' + holiday['type'].replace('national', 'NACIONAL')}" for holiday in data]), inline=False)
    embed.add_field(name="➢ INFOS", value='• As datas estão no formato Ano/Mês/Dia (Padrão ISO Date) (¬‿¬)', inline=False)


    embed.set_author(name=f"ㅤㅤㅤㅤㅤㅤㅤㅤCONSULTA DE FERIADOS {feriados}ㅤㅤㅤㅤㅤㅤㅤㅤ", icon_url='')

    embed.set_footer(text='Requested By {}'.format(ctx.author), icon_url=ctx.author.avatar_url)

    await ctx.send(embed=embed)
    
##GERADORES
    
@client.command()
async def gerador(ctx):
    embed = discord.Embed(
        title='',
        description='',
        colour=6356774
    )

    embed.add_field(name="👥 GERADOR DE PESSOA", value="Use o comando ***a!gerarpessoa*** para gerar uma pessoa.",
                    inline=False)
    embed.add_field(name="💳 GERADOR DE CARTÃO",
                    value="Use o comando ***a!gerarcartao*** para gerar um cartão Debito/Crédito.", inline=False)
    embed.add_field(name="📁 GERADOR DE E-MAIL",
                    value="Use o comando ***a!geraremail*** para gerar um e-mail aleatório.", inline=False)
    embed.add_field(name="🔆 GERADOR DE CPF", value="Use o comando ***a!gerarcpf*** para gerar e validar um CPF.",
                    inline=False)
    embed.add_field(name="🎮 GERADOR DE USERNAME", value="Use o comando ***a!gerarusr*** para gerar um username.",
                    inline=False)
    embed.add_field(name="🔐 GERADOR DE SENHA", value="Use o comando ***a!gerarsenha*** para gerar uma senha.",
                    inline=False)
    embed.add_field(name="🚙 GERADOR DE VEÍCULO", value="Use o comando ***a!gerarveiculo*** para gerar um veículo.",
                    inline=False)
    embed.add_field(name="📞 GERADOR DE NÚMERO TELEFONE",
                    value="Use o comando ***a!gerartel*** para gerar um telefone.", inline=False)
    embed.add_field(name="📲 GERADOR DE IMEI", value="Use o comando ***a!gerarimei*** para gerar um IMEI.",
                    inline=False)

    embed.set_image(url='')

    embed.set_author(name='ALIEN.py', icon_url='')

    embed.set_footer(text='ALIEN.py © All Rights Reserved', icon_url='')

    await ctx.send(embed=embed)


##FERRAMENTE PARA TESTAR PING    
    
@client.command()
async def ping(ctx):
    embed = discord.Embed(
        title='',
        colour=29695
    )


    embed.add_field(name='➢ Ping do usuário', value=f"{round(client.latency * 500)} ms", inline=False)
    embed.add_field(name='➢ Ping do servidor', value=f"{round(client.latency * 1000)} ms", inline=False)

    embed.set_author(name='ㅤㅤㅤCONSULTA DE PINGㅤㅤㅤㅤ', icon_url='')

    embed.set_image(url='')

    embed.set_footer(text='Requested By {}'.format(ctx.author), icon_url=ctx.author.avatar_url)

    await ctx.send(embed=embed)

    
 #--------------------------------------------------------[TRADUÇÃO]-------------------------------------------------------------#

@client.command() #𝐶𝑂𝑁𝑆𝑈𝐿𝑇𝐴 𝐷𝐸 𝐹𝐸𝑅𝐼𝐴𝐷𝑂𝑆
async def traduzir(ctx):    
    embed = discord.Embed(
        title='',
        colour=29695
    )
    
    embed.set_thumbnail(url="https://cdn.iconscout.com/icon/free/png-256/languages-1891105-1598018.png")

    embed.add_field(name="➢ COMANDO PARA TRADUÇÃO", value='**/tradutor "Texto" LÍNGUA (Exemplo: en, es, pt)**', inline=False)

    embed.set_footer(text='Requested By {}'.format(ctx.author), icon_url=ctx.author.avatar_url)

    await ctx.send(embed=embed)
    
    #--------------------------------------------------------[TRADUÇÃO]-------------------------------------------------------------#

@client.command() #𝐶𝑂𝑁𝑆𝑈𝐿𝑇𝐴 𝐷𝐸 𝐹𝐸𝑅𝐼𝐴𝐷𝑂𝑆
async def tradutor(ctx, phrase, *, lang):    
    embed = discord.Embed(
        title='',
        colour=29695
    )
    
    translator = Translator()

    phrase_translate = translator.translate(f"{phrase}", dest=lang)
    
    embed.set_thumbnail(url="https://cdn.iconscout.com/icon/free/png-256/languages-1891105-1598018.png")

    embed.add_field(name=f"➢ TEXTO TRADUZIDO PARA {lang.upper()}", value=f"{phrase_translate.text}", inline=False)

    embed.set_footer(text='Requested By {}'.format(ctx.author), icon_url=ctx.author.avatar_url)
   
    await ctx.send(embed=embed)
    
    #--------------------------------------------------------[GIT]-------------------------------------------------------------#
    
@client.command()
async def git(ctx):
    embed = discord.Embed(
        title='➢ CONHEÇA O REPOSITÓRIO DOS DESENVOLVEDORES',
        colour=29695
    )
    
    embed.set_thumbnail(url="https://img.icons8.com/ios-glyphs/60/ffffff/github.png")

    embed.add_field(name=f"LINKS", value=f"💣 Discord el Marlboro#8779: https://github.com/victorftrdba \n💣 Discord ALIEN#7278: https://github.com/ALIENxp", inline=False)

    embed.set_footer(text='Requested By {}'.format(ctx.author), icon_url=ctx.author.avatar_url)
   
    await ctx.send(embed=embed)
    
       
@client.command()
async def ajuda(ctx):
    embed = discord.Embed(
        title='',
        description='',
        colour=16766208
    )

    embed.add_field(name="🔐 Moderação", value='Use o comando `/admin` para ver os comandos administrativos. Comando de moderação existentes: `/kick`, `/ban`, `unban`, `/unmute`, `/role`, `/mute`, `/clear` ', inline=False)
    embed.add_field(name="🔍 Consultas", value='Use o comando `/consulta` para obter mais informações. Comandos de consultas disponíveis: `/nome`, `/cpf`, `/telefone`, `/cnpj`, `/placa`, `/ip` `/bin`, `/cep`, `/covid`, `/banco`, `/site`', inline=False)
    embed.add_field(name="🎵 Músicas", value='Use o comando `/musica` para vizualizar os comandos. Comandos acessíveis a classe: `/play`, `/stop`, `/pause`, `/resume`, `/back/`, `/skip`, `/disconnect`', inline=False)
    embed.add_field(name="🪐 Informações", value='Use o comando `/info` para ver os comandos disponíveis. Comandos existentes: `/ajuda`, `/ping`, `/git`, `/serverinfo`, `/userinfo`', inline=False)
    embed.add_field(name="🉐 Tradutor", value='Use o comando `/traduzir` "Texto" Língua (Exemplo: en, es, pt, ru)', inline=False)
    embed.add_field(name="🎓 Diversos", value='Use o comando `/diversos` para vizualizar os comandos. Comandos disponíveis: `/cotacao`, `/traduzir`', inline=False)

    embed.set_author(name='🔮 Artic Helper', icon_url='')

    await ctx.author.send(embed=embed); 


client.run('OTI3OTgxNzc4NDE5OTk4NzUw.YdSIYQ.jzB9TOCJsECFmCg66yXf7VMPPk4')
