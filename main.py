from dataclasses import replace
import dataclasses
from ntpath import join
from optparse import Values
import discord
import json
import requests
import os
from googletrans import Translator
from typing import Text
from discord.ext import commands

client = commands.Bot(command_prefix="/", case_insensitive=True, help_command=None)

@client.event
async def on_ready():
    activity = discord.Game(name='Arctic Bot | /ajuda', type=3)
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

@client.event
async def on_member_join(member):
    embed=discord.Embed(
        title="Bem vindo!",
        description="{member.mention} "
    )
    
#--------------------------------------------------------[DISPONÍVEIS]-------------------------------------------------------#

@client.command() #CONSULTAS DISPONÍVEIS
async def consulta(ctx):
    embed = discord.Embed(title='',)

    embed.add_field(name="🕵🏻‍♂️ CONSULTA POR NOME",
                    value="Use o comando `/nome` {NOME COMPLETO} para realizar a consulta.", inline=False)
    embed.add_field(name="👽 CONSULTA POR CPF",
                    value="Use o comando `/cpf` {CPF DA PESSOA} para a consultar os dados.", inline=False)
    embed.add_field(name="📵 CONSULTA POR TELEFONE",
                    value="Use o comando `/telefone` {TELEFONE} para realizar a consulta.", inline=False)
    embed.add_field(name="🏨 CONSULTA DE CNPJ",
                    value="Use o comando `/cnpj` {CNPJ} para consultar os dados.", inline=False)
    embed.add_field(name="🚘 CONSULTA POR PLACA",
                    value="Use o comando `/placa` {PLACA DO VEÍCULO} para realizar a consulta.", inline=False)
    embed.add_field(name="📌 CONSULTA DE IP",
                    value="Use o comando `/ip` {IP} para realizar a consulta do IP.", inline=False)
    embed.add_field(name="💳 CONSULTA DE BIN",
                    value="Use o comando `/bin` {NÚMERO DA BIN} para realizar a consulta.", inline=False)
    embed.add_field(name="📫 CONSULTA DE CEP",
                    value="Use o comando `/cep` {CEP DA RUA} para realizar a consulta.", inline=False)
    embed.add_field(name="🦠 CONSULTA DE COVID19",
                    value="Use o comando `/covid` {SIGLA DO ESTADO} para realizar a consulta.", inline=False)
    embed.add_field(name="🏦 CONSULTA DE CÓDIGO BANCÁRIO",
                    value="Use o comando `/banco` {CÓDIGO DO BANCO} para realizar a consulta.", inline=False)
    embed.add_field(name="💾 CONSULTA DE SITES",
                    value="Use o comando `/site` {URL DO SITE} para realizar a consulta.", inline=False)
    embed.add_field(name="📴 CONSULTA DE OPERADORA",
                    value="Use o comando `/operadora` {NÚMERO DE CELULAR} para realizar a consulta.", inline=False)    
    embed.add_field(name="🤖 CONSULTA DE E-MAIL",
                    value="Use o comando `/email` {EMAIL} para realizar a consulta.", inline=False)    
    embed.set_image(url='https://i.gifer.com/Cewn.gif')
    embed.set_author(name='Arctic', icon_url='')
    embed.set_footer(text='Arctic © All Rights Reserved', icon_url='')
    await ctx.send(embed=embed)

#--------------------------------------------------------[AJUDA]-------------------------------------------------------#

@client.command() #DIVERSOS
async def diversos(ctx):
    embed = discord.Embed(title='')
    
    embed.add_field(name="💰 CONSULTA DE COTAÇÃO",
                    value="Use o comando `/cotacao` {PAR DE MOEDA} para realizar a consulta.", inline=False)
    embed.add_field(name="🏙️ CONSULTA DE CIDADE POR DDD",
                    value="Use o comando `/ddd` {DDD} para realizar a consulta do IP.", inline=False)
    embed.add_field(name="💼 CONSULTA DE FERIADOS",
                    value="Use o comando `/feriados` {ANO} para realizar a consulta.", inline=False)
    embed.set_author(name='Arctic', icon_url='')
    embed.set_footer(text='Arctic © All Rights Reserved', icon_url='')
    await ctx.send(embed=embed)

#--------------------------------------------------------[AJUDA]-------------------------------------------------------#

@client.command() #COMANDO DE AJUDA
async def ajuda(ctx):
    embed = discord.Embed(title='')
    
    embed.add_field(name="ㅤ", value='Olá, estou aqui para te ajudar! Aqui está algum dos comandos que o Arctic possui. Ficou com alguma dúvida em relação aos comandos abaixo? Digite `/[NOME DO COMANDO]`. Exemplo: `/admin`  ', inline=False)
    embed.add_field(name="🔐 Moderação", value='Use o comando `/admin` para ver os comandos administrativos. Comando de moderação existentes: `/kick`, `/ban`, `/unban`, `/unmute`, `/role`, `/mute`, `/clear` ', inline=False)
    embed.add_field(name="🔍 Consultas", value='Use o comando `/consulta` para obter mais informações. Comandos de consultas disponíveis: `/nome`, `/cpf`, `/telefone`, `/cnpj`, `/placa`, `/ip` `/bin`, `/cep`, `/covid`, `/banco`, `/site`, `/operadora`, `/email`.', inline=False)
    embed.add_field(name="🎵 Músicas", value='Use o comando `/musica` para vizualizar os comandos. Comandos acessíveis a classe: `/play`, `/stop`, `/pause`, `/resume`, `/back`, `/skip`, `/disconnect`', inline=False)
    embed.add_field(name="🪐 Informações", value='Use o comando `/info` para ver os comandos disponíveis. Comandos existentes: `/ajuda`, `/ping`, `/git`, `/serverinfo`, `/userinfo`', inline=False)
    embed.add_field(name="🎓 Diversos", value='Use o comando `/diversos` para vizualizar os comandos. Comandos disponíveis: `/cotacao`, `/ddd`, `/feriados`, `/traduzir`', inline=False)    
    embed.add_field(name="🉐 Tradutor", value='Use o comando `/traduzir` "Texto" Língua (Exemplo: en, es, pt, ru)', inline=False)
    embed.set_image(url="https://i.imgur.com/Qkn02zM.jpg")
    embed.set_author(name='Arctic Helper', icon_url='')
    await ctx.author.send(embed=embed); 

#--------------------------------------------------------[NOME]-------------------------------------------------------#

@client.command() #CONSULTA DE NOME
async def nome(ctx):
    embed = discord.Embed(title='', description='A Consulta por ***NOME*** estará disponível em breve. No momento,\nestamos com ***ausência*** das APIs de consultas por ***nome***!',)

    embed.set_author(name='ㅤㅤㅤㅤㅤㅤㅤㅤCONSULTA DE NOMEㅤㅤㅤㅤㅤㅤㅤㅤ', icon_url='')
    embed.set_footer(text='Requested By {}'.format(ctx.author), icon_url=ctx.author.avatar_url)
    await ctx.send(embed=embed)

#--------------------------------------------------------[CPF]---------------------------------------------------------#

@client.command() #CONSULTA DE CPF
async def cpf(ctx):

    embed = discord.Embed(title='', description='A Consulta por ***CPF*** estará disponível em breve. No momento,\nestamos com ***ausência*** das APIs de consultas por ***CPF!***',)

    embed.add_field(name="• CPF", value='SEM INFORMAÇÃO', inline=False)
    embed.add_field(name="• CNS", value='SEM INFORMAÇÃO', inline=False)
    embed.add_field(name="• RG", value='SEM INFORMAÇÃO', inline=False)
    embed.add_field(name="• TÍTULO ELEITORAL", value='SEM INFORMAÇÃO', inline=False)
    embed.add_field(name="• NOME", value='SEM INFORMAÇÃO', inline=False)
    embed.add_field(name="• NASCIMENTO", value='SEM INFORMAÇÃO', inline=False)
    embed.add_field(name="• IDADE", value='SEM INFORMAÇÃO', inline=False)
    embed.add_field(name="• SIGNO", value='SEM INFORMAÇÃO', inline=False)
    embed.add_field(name="• SEXO", value='SEM INFORMAÇÃO', inline=False)
    embed.add_field(name="• COR", value='SEM INFORMAÇÃO', inline=False)
    embed.add_field(name="• MÃE", value='SEM INFORMAÇÃO', inline=False)
    embed.add_field(name="• PAI", value='SEM INFORMAÇÃO', inline=False)
    embed.add_field(name="• CIDADE DE NASCIMENTO", value='SEM INFORMAÇÃO', inline=False)
    embed.add_field(name="• ESTADO DE NASCIMENTO", value='SEM INFORMAÇÃO', inline=False)
    embed.add_field(name="• LOGRADOURO", value='SEM INFORMAÇÃO', inline=False)
    embed.add_field(name="• NÚMERO", value='SEM INFORMAÇÃO', inline=False)
    embed.add_field(name="• COMPLEMENTO", value='SEM INFORMAÇÃO', inline=False)
    embed.add_field(name="• BAIRRO", value='SEM INFORMAÇÃO', inline=False)
    embed.add_field(name="• CIDADE", value='SEM INFORMAÇÃO', inline=False)
    embed.add_field(name="• ESTADO", value='SEM INFORMAÇÃO', inline=False)
    embed.add_field(name="• PAÍS", value='SEM INFORMAÇÃO', inline=False)
    embed.add_field(name="• CEP", value='SEM INFORMAÇÃO', inline=False)
    embed.add_field(name="• E-MAIL", value='SEM INFORMAÇÃO', inline=False)
    embed.add_field(name="• TELEFONE", value='SEM INFORMAÇÃO', inline=False)
    embed.add_field(name="ㅤ", value='🐻‍❄️ﾠ**BY ARCTIC BOT**', inline=False)        
    embed.set_author(name='ㅤㅤㅤㅤㅤㅤㅤㅤCONSULTA DE CPFㅤㅤㅤㅤㅤㅤㅤㅤ', icon_url='')
    embed.set_footer(text='Requested By {}'.format(ctx.author), icon_url=ctx.author.avatar_url)
    await ctx.send(embed=embed)

#--------------------------------------------------------[TELEFONE]-------------------------------------------------------------#

@client.command() #CONSULTA DE TELEFONE
async def telefone(ctx):
    embed = discord.Embed(title='', description='A Consulta por ***TELEFONE*** estará disponível em breve. No momento,\nestamos com ***ausência*** das APIs de consultas por ***telefone!***',)

    embed.add_field(name="• TELEFONE", value='SEM INFORMAÇÃO', inline=False)
    embed.add_field(name="• NOME", value='SEM INFORMAÇÃO', inline=False)
    embed.add_field(name="• CPF/CNPJ", value='SEM INFORMAÇÃO', inline=False)
    embed.add_field(name="• LOGRADOURO", value='SEM INFORMAÇÃO', inline=False)
    embed.add_field(name="• NÚMERO", value='SEM INFORMAÇÃO', inline=False)
    embed.add_field(name="• COMPLEMENTO", value='SEM INFORMAÇÃO', inline=False)
    embed.add_field(name="• BAIRRO", value='SEM INFORMAÇÃO', inline=False)
    embed.add_field(name="• CIDADE", value='SEM INFORMAÇÃO', inline=False)
    embed.add_field(name="• ESTADO", value='SEM INFORMAÇÃO', inline=False)
    embed.add_field(name="• CEP", value='SEM INFORMAÇÃO', inline=False)
    embed.add_field(name="ㅤ", value='🐻‍❄️ﾠ**BY ARCTIC BOT**', inline=False)        
    embed.set_author(name='ㅤㅤㅤㅤㅤㅤㅤㅤCONSULTA DE TELEFONEㅤㅤㅤㅤㅤㅤㅤㅤ', icon_url='')
    embed.set_footer(text='Requested By {}'.format(ctx.author), icon_url=ctx.author.avatar_url)
    await ctx.send(embed=embed)

#--------------------------------------------------------[PLACA]-------------------------------------------------------------#

@client.command()
async def placa(ctx, placa = None):
    data = requests.get('https://apicarros.com/v1/consulta/{placa}/json', verify = False).json() # JSQ7436    
    
    try:
        embed = discord.Embed(title='')
        
        validatePlaca = data["placa"] if data["placa"] != "" else "Não encontrado"
        validateMarca = data["marca"] if data["marca"] != "Contacte o suporte 44-991559009 ou wa.me/5544991559009 " else "Não encontrado"
        validateAno = data["ano"] if data["ano"] != "" else "Não encontrado"
        validateDataAtt = data["data"] if data["data"] != "" else "Não encontrado"
        validateModelo = data["modelo"] if data["modelo"] != "Contacte o suporte 44-991559009 ou wa.me/5544991559009" else "Não encontrado"
        validateAnoModelo = data["anoModelo"] if data["anoModelo"] != "" else "Não encontrado"
        validateCor = data["cor"] if data["cor"] != "Contacte o suporte 44-991559009 ou wa.me/5544991559009" else "Não encontrado"
        validateChassi = data["chassi"] if data["chassi"] != "" else "Não encontrado"
        validateMunicipioPlaca = data["municipio"] if data["municipio"] != "Contacte o suporte 44-991559009 ou wa.me/5544991559009" else "Não encontrado"
        validateUfPlaca = data["uf"] if data["uf"] != "" else "Não encontrado"
        validateErrosPlaca = data["mensagemRetorno"] if data["mensagemRetorno"] != "Contacte o suporte 44-991559009 ou wa.me/5544991559009" else "Não encontrado"
        validateAlarmeAtt = data["dataAtualizacaoAlarme"] if data["dataAtualizacaoAlarme"] != "" else "Não encontrado"
        validateModificacao = data["dataAtualizacaoCaracteristicasVeiculo"] if data["dataAtualizacaoCaracteristicasVeiculo"] != "" else "Não encontrado"
        validateFurto = data["dataAtualizacaoRouboFurto"] if data["dataAtualizacaoRouboFurto"] != "" else "Não encontrado"
        
        embed.add_field(name="• PLACA", value=validatePlaca, inline=False)
        embed.add_field(name="• MARCA", value=validateMarca, inline=False)
        embed.add_field(name="• ANO", value=validateAno, inline=False)
        embed.add_field(name="• DATA DE ATUALIZAÇÃO ", value=validateDataAtt, inline=False)
        embed.add_field(name="• MODELO", value=validateModelo, inline=False)
        embed.add_field(name="• ANO DO MODELO", value=validateAnoModelo, inline=False)
        embed.add_field(name="• COR", value=validateCor, inline=False)
        embed.add_field(name="• CHASSI", value=validateChassi, inline=False)
        embed.add_field(name="• CIDADE", value=validateMunicipioPlaca, inline=False)
        embed.add_field(name="• ESTADO", value=validateUfPlaca, inline=False)
        embed.add_field(name="• IRREGULARIDADE", value=validateErrosPlaca, inline=False)
        embed.add_field(name="• ALARME ATUALIZADO EM", value=validateAlarmeAtt, inline=False)
        embed.add_field(name="• DATA DE MODIFICAÇÃO", value=validateModificacao, inline=False)
        embed.add_field(name="• ATUALIZAÇÃO DE FURTO", value=validateFurto, inline=False)
        embed.add_field(name="ㅤ", value='🐻‍❄️ﾠ**BY ARCTIC BOT**', inline=False)        
        embed.set_author(name='ㅤㅤㅤㅤㅤㅤㅤㅤCONSULTA DE PLACAㅤㅤㅤㅤㅤㅤㅤㅤ', icon_url='')
        embed.set_footer(text='Requested By {}'.format(ctx.author), icon_url=ctx.author.avatar_url)
        await ctx.send(embed=embed)
    
        return
    except Exception:
        pass

        embed = discord.Embed(title='')

    if (placa == None):
        embed.set_author(name='ㅤㅤㅤㅤ🤖 COMANDO PLACAㅤㅤㅤ', icon_url='')
        embed.add_field(name="Use o comando: `/placa` e a {PLACA} que deseja.", value='*Exemplo: `/placa` AAA1234*', inline=False)
        embed.add_field(name="Observação:", value='*Não utilize pontos, hifens e caracteres especiais*', inline=False)        
        return await ctx.send(embed=embed)
    else:
       embed.set_author(name='ㅤㅤㅤㅤERRO AO CONSULTAR PLACAㅤㅤㅤ', icon_url='')
       return await ctx.send(embed=embed)

#--------------------------------------------------------[CNPJ]-------------------------------------------------------------#

@client.command() #CONSULTA DE CNPJ
async def cnpj(ctx, cnpj = None):
    data = requests.get(f"https://brasilapi.com.br/api/cnpj/v1/{cnpj}").json()
    
    try:
        embed = discord.Embed(title='')
        
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
        validateFilial = data["descricao_motivo_situacao_cadastral"] if data["descricao_motivo_situacao_cadastral"] != "" else "Não encontrado"
        validateDataSituacao = data["data_situacao_cadastral"] if data["data_situacao_cadastral"] != "" else "Não encontrado"
        validateJuridica = data["codigo_natureza_juridica"] if data["codigo_natureza_juridica"] != "" else "Não encontrado"
        validateLogradouro = data["logradouro"] if data["logradouro"] != "" else "Não encontrado"
        validateTelefone1 = data["ddd_telefone_1"] if data["ddd_telefone_1"] != "" else "Não encontrado"
        validateQualificacao = data["qualificacao_do_responsavel"] if data["qualificacao_do_responsavel"] != "" else "Não encontrado"
        validateCapital = data["capital_social"] if data["capital_social"] != "" else "Não encontrado"
        validateDescricaoPorte = data["descricao_porte"] if data["descricao_porte"] != "" else "Não encontrado"
        validateSimples = data["opcao_pelo_simples"] if data["opcao_pelo_simples"] != "" else "Não encontrado"
        validateSimplesDate = data["data_opcao_pelo_simples"] if data["data_opcao_pelo_simples"] != "" else "Não encontrado"
        validateCep = data["cep"] if data["cep"] != "" else "Não encontrado"
        
        embed.add_field(name="• CNPJ", value=validateCnpj, inline=False)
        embed.add_field(name="• NOME FANTASIA", value=validateNome, inline=False)
        embed.add_field(name="• RAZÃO SOCIAL", value=validateRazao, inline=False)
        embed.add_field(name="• MATRIZ FILIAL", value=validateMatriz, inline=False)
        embed.add_field(name="• MOTIVO DA ABERTURA", value=validateFilial, inline=False)
        embed.add_field(name="• DATA SITUAÇÃO CADASTRAL", value=validateDataSituacao, inline=False)
        embed.add_field(name="• NATUREZA JURÍDICA", value=validateJuridica, inline=False)
        embed.add_field(name="• QUALIFICAÇÃO DO RESPONSÁVEL", value=validateQualificacao, inline=False)
        embed.add_field(name="• CAPITAL SOCIAL", value=validateCapital, inline=False)
        embed.add_field(name="• DESCRIÇÃO DO PORTE", value=validateDescricaoPorte, inline=False)
        embed.add_field(name="• OPÇÃO PELO SIMPLES", value=validateSimples, inline=False)
        embed.add_field(name="• DATA OPÇÃO PELO SIMPLES", value=validateSimplesDate, inline=False)
        embed.add_field(name="• STATUS", value=validateStatus, inline=False)
        embed.add_field(name="• LOGRADOURO", value=validateLogradouro, inline=False)
        embed.add_field(name="• NÚMERO", value=validateNumero, inline=False)
        embed.add_field(name="• MUNICÍPIO", value=validateMunicipio, inline=False)
        embed.add_field(name="• BAIRRO", value=validateBairro, inline=False)
        embed.add_field(name="• COMPLEMENTO", value=validateComplemento, inline=False)
        embed.add_field(name="• CEP", value=validateCep, inline=False)
        embed.add_field(name="• UF - Unidade Federativa", value=validateUf, inline=False)
        embed.add_field(name="• TELEFONE ", value=validateTelefone1, inline=False)
        embed.add_field(name="• DATA DE ABERTURA", value=validateData, inline=False)
        embed.add_field(name="• CNAE", value=validateCnae, inline=False)
        embed.add_field(name="• CNAE FISCAL", value=validateCnaeCod, inline=False)
        embed.add_field(name="ㅤ", value='🐻‍❄️ﾠ**BY ARCTIC BOT**', inline=False)        
        embed.set_author(name='ㅤㅤㅤㅤㅤㅤㅤㅤCONSULTA DE CNPJㅤㅤㅤㅤㅤㅤㅤㅤ', icon_url='')
        embed.set_footer(text='Requested By {}'.format(ctx.author), icon_url=ctx.author.avatar_url)
        await ctx.send(embed=embed)
    
        return
    except Exception:
        pass

        embed = discord.Embed(title='')

    if (cnpj == None):
        embed.set_author(name='ㅤㅤㅤㅤ🤖 COMANDO CNPJㅤㅤㅤ', icon_url='')
        embed.add_field(name="Use o comando: `/cnpj` e o {CNPJ} que deseja.", value='*Exemplo: `/cnpj` 12345678901234*', inline=False)
        embed.add_field(name="Observação:", value='*Não utilize pontos, hifens e caracteres especiais*', inline=False)        
        return await ctx.send(embed=embed)
    else:
       embed.set_author(name='ㅤㅤㅤㅤCNPJ NÃO ENCONTRADOㅤㅤㅤ', icon_url='')
       return await ctx.send(embed=embed)

#--------------------------------------------------------[IP]-------------------------------------------------------------#

@client.command() #CONSULTA DE IP
async def ip(ctx, ip = None):
    data = requests.get(f"http://ipwhois.app/json/{ip}").json()
    
    try:
        embed = discord.Embed(title='')

        validateAsn = data["asn"] if data["asn"] != "" else "Não encontrado"

        embed.add_field(name="• IP", value=data['ip'], inline=False)
        embed.add_field(name="• CIDADE", value=data['city'], inline=False)
        embed.add_field(name="• ESTADO", value=data['region'], inline=False)
        embed.add_field(name="• PAÍS", value=data['country'], inline=False)
        embed.add_field(name="• CONTINENTE", value=data["continent"], inline=False)
        embed.add_field(name="• LATITUDE", value=data['latitude'], inline=False)
        embed.add_field(name="• LONGITUDE", value=data['longitude'], inline=False)
        embed.add_field(name="• PROVEDOR", value=data['isp'], inline=False)
        embed.add_field(name="• ASN", value=validateAsn, inline=False)
        embed.add_field(name="• EMPRESA RESPONSÁVEL", value=data['org'], inline=False)
        embed.add_field(name="• TIPO DE CONEXÃO", value=data['type'], inline=False)
        embed.add_field(name="ㅤ", value='🐻‍❄️ﾠ**BY ARCTIC BOT**', inline=False)        
        embed.set_author(name='ㅤㅤㅤㅤㅤㅤㅤㅤCONSULTA DE IPㅤㅤㅤㅤㅤㅤㅤㅤ', icon_url='')
        embed.set_footer(text='Requested By {}'.format(ctx.author), icon_url=ctx.author.avatar_url)
        await ctx.send(embed=embed)

        return
    except Exception:
        pass
         
        embed = discord.Embed(title='')
    
    if (ip == None):
        embed.set_author(name='ㅤㅤㅤㅤ🤖 COMANDO IPㅤㅤㅤ', icon_url='')
        embed.add_field(name="Use o comando: `/ip` e o {IP} que deseja.", value='*Exemplo: `/ip` 127.0.0.1*', inline=False)
        return await ctx.send(embed=embed)
    else:
       embed.set_author(name='ㅤㅤㅤIP NÃO ENCONTRADOㅤㅤㅤ', icon_url='')
       return await ctx.send(embed=embed)

#--------------------------------------------------------[COVID19]-------------------------------------------------------------#

@client.command() #CONSULTA DE COVID19
async def covid(ctx, covid = None):
    data = requests.get(f"https://covid19-brazil-api.vercel.app/api/report/v1/brazil/uf/{covid}").json()

    try:
        embed = discord.Embed(title='')

        embed.add_field(name="• ESTADO", value=data['state'], inline=False)
        embed.add_field(name="• CASOS", value=data['cases'], inline=False)
        embed.add_field(name="• MORTES", value=data['deaths'], inline=False)
        embed.add_field(name="• SUSPEITOS", value=data['suspects'], inline=False)
        embed.add_field(name="• DESCARTADOS", value=data['refuses'], inline=False)
        embed.add_field(name="• DATA DE ATUALIZAÇÃO", value=data['datetime'], inline=False)
        embed.add_field(name="ㅤ", value='🐻‍❄️ﾠ**BY ARCTIC BOT**', inline=False)        
        embed.set_author(name='ㅤㅤㅤㅤㅤㅤㅤㅤCONSULTA DE COVID19ㅤㅤㅤㅤㅤㅤㅤㅤ', icon_url='')
        embed.set_footer(text='Requested By {}'.format(ctx.author), icon_url=ctx.author.avatar_url)
        await ctx.send(embed=embed)
        
        return
    except Exception:
        pass

        embed = discord.Embed(title='')

    if (covid == None):
        embed.set_author(name='ㅤㅤㅤㅤ🤖 COMANDO COVIDㅤㅤㅤ', icon_url='')
        embed.add_field(name="Use o comando: `/covid` e o {ESTADO} que deseja.", value='*Exemplo*: `/covid SP`', inline=False)
        embed.add_field(name="Observação:", value='*Utilize apenas a sigla do estado correspondente!*', inline=False)
        embed.add_field(name="Estados Brasileiros com suas respectivas siglas:", value='Acre - `AC`\nAlagoas - `AL`\nAmazonas - `AM`\nBahia - `BA`\nCeará - `CE`\nDistrito Federal - `DF`\nEspírito Santo - `ES`\nGoiás - `GO`\nMaranhão - `MA`\nMato Grosso - `MT`\nMato Grosso do Sul - `MS`\nMinas Gerais - `MG`\nPará - `PA`\nParaíba - `PB`\nParaná - `PR`\nPernambuco - `PE`\nPiauí - `PI`\nRio de Janeiro - `RJ`\nRio Grande do Norte - `RN`\nRio Grande do Sul - `RS`\nRondônia - `RO`\nRoraima	- `RR`\nSanta Catarina - `SC`\nSão Paulo - `SP`\nSergipe - `SE`\nTocantins - `TO`\n', inline=False)
        return await ctx.send(embed=embed)
    else:
       embed.set_author(name='ㅤㅤㅤㅤㅤESTADO INVÁLIDOㅤㅤㅤ', icon_url='')
       embed.add_field(name="ㅤ", value="*Utilize o comando: `/covid` para obter mais informações.* ", inline=False)
       return await ctx.send(embed=embed)

#--------------------------------------------------------[CEP]-------------------------------------------------------------#

@client.command() #CONSULTA DE CEP
async def cep(ctx, cep = None):
    data = requests.get(f"https://cep.awesomeapi.com.br/json/{cep}").json()

    try:
        embed = discord.Embed(title='')

        embed.add_field(name="• CEP", value=data['cep'], inline=False)
        embed.add_field(name="• LOGRADOURO", value=data['address'], inline=False)
        embed.add_field(name="• BAIRRO", value=data['district'], inline=False)
        embed.add_field(name="• CIDADE", value=data['city'], inline=False)
        embed.add_field(name="• ESTADO", value=data['state'], inline=False)
        embed.add_field(name="• LATITUDE", value=data['lat'], inline=False)
        embed.add_field(name="• LONGITUDE", value=data['lng'], inline=False)
        embed.add_field(name="• IBGE", value=data['city_ibge'], inline=False)
        embed.add_field(name="• DDD", value=data['ddd'], inline=False)
        embed.add_field(name="ㅤ", value='🐻‍❄️ﾠ**BY ARCTIC BOT**', inline=False)        
        embed.set_author(name='ㅤㅤㅤㅤㅤㅤㅤㅤCONSULTA DE CEPㅤㅤㅤㅤㅤㅤㅤㅤ', icon_url='')
        embed.set_footer(text='Requested By {}'.format(ctx.author), icon_url=ctx.author.avatar_url)
        await ctx.send(embed=embed)

        return
    except Exception:
        pass

        embed = discord.Embed(title='')

    if (cep == None):
        embed.set_author(name='ㅤㅤㅤㅤ🤖 COMANDO CEPㅤㅤㅤ', icon_url='')
        embed.add_field(name="Use o comando: `/cep` e o {CEP} que deseja.", value='*Exemplo*: `/cep 70150904`', inline=False)
        embed.add_field(name="Observação:", value='*Não utilize pontos, hifens e caracteres especiais*', inline=False)        
        return await ctx.send(embed=embed)
    else:
       embed.set_author(name='ㅤㅤㅤCEP NÃO ENCONTRADOㅤㅤㅤ', icon_url='')
       return await ctx.send(embed=embed)
   
#--------------------------------------------------------[BANCO]-------------------------------------------------------------#

@client.command() #CONSULTA DE CÓDIGO BANCÁRIO
async def banco(ctx, banco = None):
    data = requests.get(f"https://brasilapi.com.br/api/banks/v1/{banco}").json()

    try:
        embed = discord.Embed(title='')

        embed.add_field(name="• ISPB", value=data['ispb'], inline=False)
        embed.add_field(name="• NOME DO BANCO", value=data['name'], inline=False)
        embed.add_field(name="• CÓDIGO BANCÁRIO", value=data['code'], inline=False)
        embed.add_field(name="• INFORMAÇÕES ADICIONAIS", value=data['fullName'], inline=False)
        embed.add_field(name="ㅤ", value='🐻‍❄️ﾠ**BY ARCTIC BOT**', inline=False)        
        embed.set_author(name='ㅤㅤㅤㅤㅤㅤㅤㅤCONSULTA DE BANCOㅤㅤㅤㅤㅤㅤㅤㅤ', icon_url='')
        embed.set_footer(text='Requested By {}'.format(ctx.author), icon_url=ctx.author.avatar_url)
        await ctx.send(embed=embed)
        
        return
    except Exception:
        pass

        embed = discord.Embed(title='')

    if (banco == None):
        embed.set_author(name='ㅤㅤㅤㅤ🤖 COMANDO BANCOㅤㅤㅤ', icon_url='')
        embed.add_field(name="Use o comando: `/banco` e o {CÓDIGO DO BANCO}", value='*Exemplo*: `/banco 237`', inline=False)
        embed.add_field(name="Observação:", value='*Utilize apenas o código bancário correspondente!*', inline=False)        
        return await ctx.send(embed=embed)
    else:
       embed.set_author(name='ㅤㅤCÓDIGO BANCÁRIO NÃO ENCONTRADOㅤㅤ', icon_url='')
       return await ctx.send(embed=embed)

#--------------------------------------------------------[BIN]-------------------------------------------------------------#

@client.command() #CONSULTA DE BIN
async def bin(ctx, bin = None):
    data = requests.get(
        f"https://api.bincodes.com/bin/?format=json&api_key=c0107d14acda7e1831dfe26ee8e8b3a5&bin={bin}").json()

    try:
        embed = discord.Embed(title='')

        validateSiteBin = data["website"] if data["website"] != "" else "Não encontrado"
        validateNumeroTelefoneBin = data["phone"] if data["phone"] != "" else "Não encontrado"
        
        embed.add_field(name="• BIN", value=data['bin'], inline=False)
        embed.add_field(name="• MODELO", value=data['type'], inline=False)
        embed.add_field(name="• NÍVEL", value=data['level'], inline=False)
        embed.add_field(name="• BANDEIRA", value=data['card'], inline=False)
        embed.add_field(name="• PAÍS", value=data['country'], inline=False)
        embed.add_field(name="• SIGLA", value=data['countrycode'], inline=False)
        embed.add_field(name="• BANCO", value=data['bank'], inline=False)
        embed.add_field(name="• SITE", value=data['website'], inline=False)
        embed.add_field(name="• TELEFONE", value=data['phone'], inline=False)
        embed.add_field(name="ㅤ", value='🐻‍❄️ﾠ**BY ARCTIC BOT**', inline=False)                
        embed.set_author(name='ㅤㅤㅤㅤㅤㅤㅤㅤCONSULTA DE BINㅤㅤㅤㅤㅤㅤㅤㅤ', icon_url='')
        embed.set_footer(text='Requested By {}'.format(ctx.author), icon_url=ctx.author.avatar_url)
        await ctx.send(embed=embed)

        return
    except Exception:
        pass

        embed = discord.Embed(title='')

    if (bin == None):
        embed.set_author(name='ㅤㅤㅤㅤ🤖 COMANDO BINㅤㅤㅤ', icon_url='')
        embed.add_field(name="Use o comando: `/bin` e a {BIN} que deseja.", value='*Exemplo*: `/bin 522840`', inline=False)
        embed.add_field(name="Observação:", value='*Não utilize pontos, hifens e caracteres especiais*', inline=False)        
        return await ctx.send(embed=embed)
    else:
       embed.set_author(name='ㅤㅤㅤBIN NÃO ENCONTRADAㅤㅤㅤ', icon_url='')
       return await ctx.send(embed=embed)

#--------------------------------------------------------[SITE]-------------------------------------------------------------#

@client.command() #CONSULTA DE SITE
async def site(ctx, site = None):
    data = requests.get(f"http://ipwhois.app/json/{site}").json()

    try:
        embed = discord.Embed(title='')

        embed.add_field(name="• IP", value=data['ip'], inline=False)
        embed.add_field(name="• CIDADE", value=data['city'], inline=False)
        embed.add_field(name="• ESTADO", value=data['region'], inline=False)
        embed.add_field(name="• PAÍS", value=data['country'], inline=False)
        embed.add_field(name="• LATITUDE", value=data['latitude'], inline=False)
        embed.add_field(name="• LONGITUDE", value=data['longitude'], inline=False)
        embed.add_field(name="• ORGANIZAÇÃO", value=data['isp'], inline=False)
        embed.add_field(name="• EMPRESA", value=data['org'], inline=False)
        embed.add_field(name="• FUSO HORÁRIO", value=data['timezone'], inline=False)
        embed.add_field(name="ㅤ", value='🐻‍❄️ﾠ**BY ARCTIC BOT**', inline=False)                
        embed.set_author(name='ㅤㅤㅤㅤㅤㅤㅤㅤCONSULTA DE SITEㅤㅤㅤㅤㅤㅤㅤㅤ', icon_url='')
        embed.set_footer(text='Requested By {}'.format(ctx.author), icon_url=ctx.author.avatar_url)
        await ctx.send(embed=embed)

        return
    except Exception:
        pass

        embed = discord.Embed(title='')

    if (site == None):
        embed.set_author(name='ㅤㅤㅤㅤ🤖 COMANDO SITEㅤㅤㅤ', icon_url='')
        embed.add_field(name="Use o comando: `/site` e a {SITE} que deseja.", value='*Exemplo*: `/site google.com`', inline=False)
        return await ctx.send(embed=embed)
    else:
       embed.set_author(name='ㅤㅤㅤSITE NÃO ENCONTRADOㅤㅤㅤ', icon_url='')
       return await ctx.send(embed=embed)

#--------------------------------------------------------[OPERADORA]-------------------------------------------------------------#

@client.command() #CONSULTA DE OPERADORA
async def operadora(ctx, operadora = None):
    data = requests.get(f"http://apilayer.net/api/validate?access_key=317fca6d1dc194d6c5e5d16898b63ddf&number={operadora}&country_code=&format=1").json()
    
    try:
        embed = discord.Embed(title='')

        embed.add_field(name="• VÁLIDO", value=data['valid'], inline=False)
        embed.add_field(name="• NÚMERO", value=data['number'], inline=False)
        embed.add_field(name="• FORMATO INTERNACIONAL", value=data['international_format'], inline=False)
        embed.add_field(name="• DDI DO PAÍS", value=data['country_prefix'], inline=False)
        embed.add_field(name="• CÓDIGO DO PAÍS", value=data['country_code'], inline=False)
        embed.add_field(name="• NOME DO PAÍS", value=data['country_name'], inline=False)
        embed.add_field(name="• LOCALIZAÇÃO", value=data['location'], inline=False)
        embed.add_field(name="• OPERADORA/PROVEDOR", value=data['carrier'], inline=False)
        embed.add_field(name="• LINHA DE DISPOSITÍVO", value=data['line_type'], inline=False)
        embed.add_field(name="ㅤ", value='🐻‍❄️ﾠ**BY ARCTIC BOT**', inline=False)                
        embed.set_author(name='ㅤㅤㅤㅤㅤㅤㅤㅤCHECKER DE OPERADORAㅤㅤㅤㅤㅤㅤㅤㅤ', icon_url='')
        embed.set_footer(text='Requested By {}'.format(ctx.author), icon_url=ctx.author.avatar_url)
        await ctx.send(embed=embed)

        return
    except Exception:
        pass

        embed = discord.Embed(title='')

    if (operadora == None):
        embed.set_author(name='ㅤㅤㅤㅤ🤖 COMANDO OPERADORAㅤㅤㅤ', icon_url='')
        embed.add_field(name="Use o comando: `/operadora` e a {NÚMERO}", value='*Exemplo*: `/operadora +5511987654321`', inline=False)
        embed.add_field(name="Observação:", value='*utilize o padrão universal.*', inline=False)        
        return await ctx.send(embed=embed)
    else:
       embed.set_author(name='ㅤㅤㅤOPERADORA NÃO ENCONTRADAㅤㅤㅤ', icon_url='')
       return await ctx.send(embed=embed)

#--------------------------------------------------------[EMAIL]-------------------------------------------------------------#

@client.command() #CONSULTA DE E-MAIL
async def email(ctx, email = None):
    data = requests.get(f"http://apilayer.net/api/check?access_key=e3d07653b28027265c15d3218aaaa4c9&email={email}&smtp=1&format=1").json()
    
    try:
        embed = discord.Embed(title='')

        embed.add_field(name="• E-MAIL", value=data['email'], inline=False)
        embed.add_field(name="• USUÁRIO", value=data['user'], inline=False)
        embed.add_field(name="• DOMÍNIO", value=data['domain'], inline=False)
        embed.add_field(name="• FORMATO VALIDO", value=data['format_valid'], inline=False)
        embed.add_field(name="• CORREIO ATIVO", value=data['mx_found'], inline=False)
        embed.add_field(name="• SMTP DISPONÍVEL", value=data['smtp_check'], inline=False)
        embed.add_field(name="• FUNÇÕES ATIVAS", value=data['role'], inline=False)
        embed.add_field(name="• E-MAIL DISPONÍVEL", value=data['disposable'], inline=False)
        embed.add_field(name="• GRATUITO", value=data['free'], inline=False)
        embed.add_field(name="• PONTUAÇÃO", value=data['score'], inline=False)
        embed.add_field(name="ㅤ", value='🐻‍❄️ﾠ**BY ARCTIC BOT**', inline=False)                
        embed.set_author(name='ㅤㅤㅤㅤㅤㅤㅤㅤCHECKER DE E-MAILㅤㅤㅤㅤㅤㅤㅤㅤ', icon_url='')
        embed.set_footer(text='Requested By {}'.format(ctx.author), icon_url=ctx.author.avatar_url)
        await ctx.send(embed=embed)

        return
    except Exception:
        pass

        embed = discord.Embed(title='')

    if (email == None):
        embed.set_author(name='ㅤㅤㅤㅤ🤖 COMANDO EMAILㅤㅤㅤ', icon_url='')
        embed.add_field(name="Use o comando: `/email` e a {E-MAIL}", value='*Exemplo*: `/email google@gmail.com`', inline=False)
        return await ctx.send(embed=embed)
    else:
       embed.set_author(name='E-MAIL NÃO ENCONTRADAㅤㅤㅤ', icon_url='')
       return await ctx.send(embed=embed)
   
#--------------------------------------------------------[C0TAÇÃO]-------------------------------------------------------------#

@client.command() #COTAÇÃO DE MOEDAS
async def cotacao(ctx, cotacao = None):
    data = requests.get(f"https://economia.awesomeapi.com.br/last/{cotacao}").json()
    coin_name = cotacao.replace("-", "")
    
    try:
        embed = discord.Embed(title='')
        
        embed.add_field(name="• MOEDA A COMPARAR", value=data[coin_name]["code"], inline=False)
        embed.add_field(name="• MOEDA A SER COMPARADA", value=data[coin_name]["codein"], inline=False)
        embed.add_field(name="• NOME DAS PARIEDADES", value=data[coin_name]["name"], inline=False)
        embed.add_field(name="• MÁXIMA DO DIA", value=data[coin_name]["high"], inline=False)
        embed.add_field(name="• MÍNIMA DO DIA", value=data[coin_name]["low"], inline=False)
        embed.add_field(name="• VARIAÇÃO", value=data[coin_name]["varBid"], inline=False)
        embed.add_field(name="• PORCENTAGEM DE VARIAÇÃO", value=data[coin_name]["pctChange"], inline=False)
        embed.add_field(name="• COMPRA", value=data[coin_name]["bid"], inline=False)
        embed.add_field(name="• VENDA", value=data[coin_name]["ask"], inline=False)
        embed.add_field(name="• ATUALIZAÇÃO", value=data[coin_name]["create_date"], inline=False)
        embed.add_field(name="ㅤ", value='🐻‍❄️ﾠ**BY ARCTIC BOT**', inline=False)                
        embed.set_author(name='ㅤㅤㅤㅤㅤㅤㅤㅤCOTAÇÃO DE MOEDASㅤㅤㅤㅤㅤㅤㅤㅤ', icon_url='')
        embed.set_footer(text='Requested By {}'.format(ctx.author), icon_url=ctx.author.avatar_url)
        await ctx.send(embed=embed)

        return
    except Exception:
        pass

        embed = discord.Embed(title='')
    
    if (cotacao == None):
        embed.set_author(name='ㅤㅤㅤㅤ🤖 COMANDO COTAÇÃOㅤㅤㅤ', icon_url='')
        embed.add_field(name="Use o comando: `/cotacao` e o {PAR DE MOEDA} que deseja", value='*Exemplo*: `/cotacao BRL-USD`', inline=False)
        embed.add_field(name="Observação:", value='*O par precisa ser separado com hifen*', inline=False)        
        return await ctx.send(embed=embed)
    else:
       embed.set_author(name='ㅤㅤCOTAÇÃO DE MOEDAS INVÁLIDAㅤㅤㅤ', icon_url='')
       return await ctx.send(embed=embed)        

#--------------------------------------------------------[DDD]-------------------------------------------------------------#

@client.command() #CONSULTAS DE CIDADES POR DDDD
async def ddd(ctx, ddd = None):
    data = requests.get(f"https://brasilapi.com.br/api/ddd/v1/{ddd}").json()

    try:
        embed = discord.Embed(title='')

        embed.add_field(name="• ESTADO", value=data['state'], inline=False)
        embed.add_field(name="• CIDADES", value='\n'.join([f"{city}" for city in data["cities"]]), inline=False)
        embed.add_field(name="ㅤ", value='🐻‍❄️ﾠ**BY ARCTIC BOT**', inline=False)                
        embed.set_author(name='ㅤㅤㅤㅤㅤㅤㅤㅤCONSULTA DE CIDADES POR DDDㅤㅤㅤㅤㅤㅤㅤㅤ', icon_url='')
        embed.set_footer(text='Requested By {}'.format(ctx.author), icon_url=ctx.author.avatar_url)
        await ctx.send(embed=embed)

        return
    except Exception:
        pass

        embed = discord.Embed(title='')

    if (ddd == None):
        embed.set_author(name='ㅤㅤㅤㅤ🤖 COMANDO DDDㅤㅤㅤ', icon_url='')
        embed.add_field(name="Use o comando: `/ddd` e o {DDD} que deseja", value='*Exemplo*: `/ddd 11`', inline=False)
        return await ctx.send(embed=embed)
    else:
       embed.set_author(name='ㅤㅤDDD INVÁLIDOㅤㅤ', icon_url='')
       return await ctx.send(embed=embed)        

#--------------------------------------------------------[FERIADOS]-------------------------------------------------------------#

@client.command() #CONSULTA DE FERIADOS
async def feriados(ctx, feriados = None):
    data = requests.get(f"https://brasilapi.com.br/api/feriados/v1/{feriados}").json()

    try:
        embed = discord.Embed(title='')

        embed.add_field(name="• FERIADOS", value='\n\n'.join([f"{holiday['name'].upper() + ' ★ ' + holiday['date'].replace('-', '/') + ' ★ ' + holiday['type'].replace('national', 'NACIONAL')}" for holiday in data]), inline=False)
        embed.add_field(name="• INFO", value='As datas estão no formato Ano/Mês/Dia (Padrão ISO Date)', inline=False)
        embed.add_field(name="ㅤ", value='🐻‍❄️ﾠ**BY ARCTIC BOT**', inline=False)                
        embed.set_author(name=f"ㅤㅤㅤㅤㅤㅤㅤㅤCONSULTA DE FERIADOS {feriados}ㅤㅤㅤㅤㅤㅤㅤㅤ", icon_url='')
        embed.set_footer(text='Requested By {}'.format(ctx.author), icon_url=ctx.author.avatar_url)
        await ctx.send(embed=embed)

        return
    except Exception:
        pass

        embed = discord.Embed(title='')

    if (feriados == None):
        embed.set_author(name='ㅤㅤㅤㅤ🤖 COMANDO FERIADOSㅤㅤㅤ', icon_url='')
        embed.add_field(name="Use o comando: `/feriados` e o {ANO}", value='*Exemplo*: `/feriados 2022`', inline=False)
        embed.add_field(name="Observação:", value='*Suportado entre os anos 1900 e 2199*', inline=False)
        return await ctx.send(embed=embed)
    else:
       embed.set_author(name='ㅤㅤㅤㅤFORMATO DO ANO INVÁLIDOㅤㅤ', icon_url='')
       embed.add_field(name="ㅤ", value="*Utilize o comando: `/feriados` para obter mais informações.* ", inline=False)
       return await ctx.send(embed=embed)        

#--------------------------------------------------------[GERADOR]-------------------------------------------------------------#
    
@client.command() #GERADORES
async def gerador(ctx):

    embed = discord.Embed(title='')

    embed.add_field(name="👥 GERADOR DE PESSOA", value="Use o comando `/gerarpessoa` para gerar uma pessoa.",
                    inline=False)
    embed.add_field(name="💳 GERADOR DE CARTÃO",
                    value="Use o comando `/gerarcartao` para gerar um cartão Debito/Crédito.", inline=False)
    embed.add_field(name="📁 GERADOR DE E-MAIL",
                    value="Use o comando `/geraremail` para gerar um e-mail aleatório.", inline=False)
    embed.add_field(name="🔆 GERADOR DE CPF", value="Use o comando `/gerarcpf` para gerar e validar um CPF.",
                    inline=False)
    embed.add_field(name="🎮 GERADOR DE USERNAME", value="Use o comando `/gerarusr` para gerar um username.",
                    inline=False)
    embed.add_field(name="🔐 GERADOR DE SENHA", value="Use o comando `/gerarsenha` para gerar uma senha.",
                    inline=False)
    embed.add_field(name="🚙 GERADOR DE VEÍCULO", value="Use o comando `/gerarveiculo` para gerar um veículo.",
                    inline=False)
    embed.add_field(name="📞 GERADOR DE NÚMERO TELEFONE",
                    value="Use o comando `/gerartel` para gerar um telefone.", inline=False)
    embed.add_field(name="📲 GERADOR DE IMEI", value="Use o comando `/gerarimei` para gerar um IMEI.",
                    inline=False)
    embed.set_author(name='Arctic', icon_url='')
    embed.set_footer(text='Arctic © All Rights Reserved', icon_url='')
    await ctx.send(embed=embed)
    
#--------------------------------------------------------[GERADOR DE CC]-------------------------------------------------------------#
    
@client.command() #GERADOR DE CARTÃO
async def gerarcartao(ctx, gerarcartao = None):
    data = requests.get(
        f"https://api.bincodes.com/cc-gen/?format=json&api_key=c0107d14acda7e1831dfe26ee8e8b3a5&input={gerarcartao}").json()

    try:
        embed = discord.Embed(title='')
        
        embed.add_field(name="• BANDEIRA", value=data['card'], inline=False)
        embed.add_field(name="• CARTÃO", value=data['number'], inline=False)
        embed.add_field(name="ㅤ", value='🐻‍❄️ﾠ**BY ARCTIC BOT**', inline=False)                
        embed.set_author(name='ㅤㅤㅤㅤㅤㅤㅤㅤGERADOR DE CARTÃOㅤㅤㅤㅤㅤㅤㅤㅤ', icon_url='')
        embed.set_footer(text='Requested By {}'.format(ctx.author), icon_url=ctx.author.avatar_url)
        await ctx.send(embed=embed)

        return
    except Exception:
        pass

        embed = discord.Embed(title='')

    if (gerarcartao == None):
        embed.set_author(name='ㅤㅤㅤㅤ🤖 COMANDO GERADOR DE CARTÃOㅤㅤㅤ', icon_url='')
        embed.add_field(name="Use o comando: `/gerarcartao` e a {BANDEIRA} que deseja.", value='*Exemplo*: `/gerarcartao visa`', inline=False)
        embed.add_field(name="Observação:", value='*Utilize apenas a bandeira!*', inline=False)        
        embed.add_field(name="Bandeiras disponíveis:", value='`VISA`\n`MASTERCARD`\n`AMEX`\n`JCB`\n`DINERS`\n`MAESTRO`\n', inline=False)
        return await ctx.send(embed=embed)
    else:
       embed.set_author(name='ㅤㅤㅤERRO AO GERAR CARTÃOㅤㅤㅤ', icon_url='')
       return await ctx.send(embed=embed)

#--------------------------------------------------------[PING]-------------------------------------------------------------#

@client.command()
async def ping(ctx):
    embed = discord.Embed(title='')


    embed.add_field(name='• Ping do usuário', value=f"{round(client.latency * 500)} ms", inline=False)
    embed.add_field(name='• Ping do servidor', value=f"{round(client.latency * 1000)} ms", inline=False)
    embed.set_author(name='ㅤㅤㅤCONSULTA DE PINGㅤㅤㅤㅤ', icon_url='')
    embed.set_image(url='')
    embed.set_footer(text='Requested By {}'.format(ctx.author), icon_url=ctx.author.avatar_url)
    await ctx.send(embed=embed)

#--------------------------------------------------------[TRADUÇÃO]-------------------------------------------------------------#

@client.command() #𝐶𝑂𝑁𝑆𝑈𝐿𝑇𝐴 𝐷𝐸 𝐹𝐸𝑅𝐼𝐴𝐷𝑂𝑆
async def traduzir(ctx):    
    embed = discord.Embed(title='')
    
    embed.add_field(name="Use o comando: `/tradutor [TEXTO] LÍNGUA`", value='*Exemplo*: `/tradutor Hello en`', inline=False)
    embed.set_author(name='ㅤㅤㅤCOMANDO PARA TRADUÇÃOㅤㅤㅤㅤ', icon_url='')
    embed.set_thumbnail(url="https://cdn.iconscout.com/icon/free/png-256/languages-1891105-1598018.png")
    embed.set_footer(text='Requested By {}'.format(ctx.author), icon_url=ctx.author.avatar_url)
    await ctx.send(embed=embed)

#--------------------------------------------------------[TRADUÇÃO]-------------------------------------------------------------#

@client.command() #𝐶𝑂𝑁𝑆𝑈𝐿𝑇𝐴 𝐷𝐸 𝐹𝐸𝑅𝐼𝐴𝐷𝑂𝑆
async def tradutor(ctx, phrase, *, lang):    
    embed = discord.Embed(title='')
    
    translator = Translator()

    phrase_translate = translator.translate(f"{phrase}", dest=lang)
    
    embed.set_thumbnail(url="https://cdn.iconscout.com/icon/free/png-256/languages-1891105-1598018.png")
    embed.add_field(name=f"TEXTO TRADUZIDO PARA {lang.upper()}", value=f"{phrase_translate.text}", inline=False)
    embed.set_footer(text='Requested By {}'.format(ctx.author), icon_url=ctx.author.avatar_url)
    await ctx.send(embed=embed)

#--------------------------------------------------------[GIT]-------------------------------------------------------------#

@client.command()
async def git(ctx):
    embed = discord.Embed(title='')
    
    embed.set_thumbnail(url="https://img.icons8.com/ios-glyphs/60/ffffff/github.png")
    embed.set_author(name='CONHEÇA O REPOSITÓRIO DOS DESENVOLVEDORES', icon_url='')
    embed.add_field(name=f"ㅤ", value=f"👽 ALIEN#7278 / Github: https://github.com/ALIENxp \n\n💥 el Marlboro#8779 / Github: https://github.com/victorftrdba \n\n", inline=False)
    embed.set_footer(text='Requested By {}'.format(ctx.author), icon_url=ctx.author.avatar_url)
    await ctx.send(embed=embed)

#--------------------------------------------------------[AJUDA]-------------------------------------------------------------#

        

client.run('OTI3OTgxNzc4NDE5OTk4NzUw.YdSIYQ._9s0Rju0_2S1FJu33zohezmyc_M')