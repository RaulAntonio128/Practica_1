

import pandas as pd 

############################################################################################################################
##########          PREESCOLAR               ##########

##########          CENDI      
PRE_D_1 = pd.read_excel('C:/Users/raul.guadalupe/Documents/Mejoredu/Bases/F911/Ciclo_2023_2024/Finales/Basica/Educación Básica/INICIAL_I2324.XLSX', sheet_name = 'INICIAL_I2324')

#Seleccionando las escuelas que ofrecen preescolar y que tienen matrícula
FILTRO = (PRE_D_1['V175'] > 0) & (PRE_D_1['V478'] > 0) 
PRE_D_2 = PRE_D_1[FILTRO]
del[FILTRO]

PRE_D_2['CCTT'] = PRE_D_2.agg('{0[CV_CCT]}{0[CV_TURNO]}'.format, axis=1)
PRE_D_2['NIVEL'] = '1'
PRE_D_2['MODALIDAD'] = '1'

# Matrícula según edad
PRE_D_2 = PRE_D_2.eval('MAT_EDAESP_H = V420+V421+V422+V793+V438+V439+V796+V451')    
PRE_D_2 = PRE_D_2.eval('MAT_EDAESP_M = V426+V427+V428+V794+V442+V443+V797+V454')    
PRE_D_2 = PRE_D_2.eval('MAT_EDAESP_T = MAT_EDAESP_H+MAT_EDAESP_M')

PRE_D_2 = PRE_D_2.eval('MAT_EDATOT_H = V419+V420+V421+V422+V423+V793+V438+V439+V440+V796+V451+V452')    
PRE_D_2 = PRE_D_2.eval('MAT_EDATOT_M = V425+V426+V427+V428+V429+V794+V442+V443+V444+V797+V454+V455')    
PRE_D_2 = PRE_D_2.eval('MAT_EDATOT_T = MAT_EDATOT_H+MAT_EDATOT_M')

#Seleccionando variables :: .LOC[] permite acceder a las columnas deseadas del DataFrame
PRE_D_3 = PRE_D_2.loc[:, ['CCTT', 'NIVEL', 'MODALIDAD', 
                             'MAT_EDAESP_H', 'MAT_EDAESP_M', 'MAT_EDAESP_T', 
                             'MAT_EDATOT_H', 'MAT_EDATOT_M', 'MAT_EDATOT_T']]   

PRE_D_3.head()
PRE_D_3.shape



##########          GENERAL      
PRE_G_1 = pd.read_excel('C:/Users/raul.guadalupe/Documents/Mejoredu/Bases/F911/Ciclo_2023_2024/Finales/Basica/Educación Básica/PREEGENERAL_I2324.XLSX', sheet_name = 'PREEGENERAL_I2324')

PRE_G_2 = PRE_G_1.loc[(PRE_G_1['V177'] >= 1)]

PRE_G_2['CCTT'] = PRE_G_2.agg('{0[CV_CCT]}{0[CV_TURNO]}'.format, axis=1)
PRE_G_2['NIVEL'] = '1'
PRE_G_2['MODALIDAD'] = '2'

# Matrícula según edad
PRE_G_2 = PRE_G_2.eval('MAT_EDAESP_H = V122+V123+V124+V977+V139+V140+V980+V151')    
PRE_G_2 = PRE_G_2.eval('MAT_EDAESP_M = V128+V129+V130+V978+V143+V144+V981+V154')    
PRE_G_2 = PRE_G_2.eval('MAT_EDAESP_T = MAT_EDAESP_H+MAT_EDAESP_M')

PRE_G_2 = PRE_G_2.eval('MAT_EDATOT_H = V121+V122+V123+V124+V125+V977+V139+V140+V141+V980+V151+V152')    
PRE_G_2 = PRE_G_2.eval('MAT_EDATOT_M = V127+V128+V129+V130+V131+V978+V143+V144+V145+V981+V154+V155')    
PRE_G_2 = PRE_G_2.eval('MAT_EDATOT_T = MAT_EDATOT_H+MAT_EDATOT_M')

#Seleccionando variables :: .LOC[] permite acceder a las columnas deseadas del DataFrame
PRE_G_3 = PRE_G_2.loc[:, ['CCTT', 'NIVEL', 'MODALIDAD', 
                             'MAT_EDAESP_H', 'MAT_EDAESP_M', 'MAT_EDAESP_T', 
                             'MAT_EDATOT_H', 'MAT_EDATOT_M', 'MAT_EDATOT_T']]   

PRE_G_3.head()
PRE_G_3.shape



##########          INDÍGENA      
PRE_I_1 = pd.read_excel('C:/Users/raul.guadalupe/Documents/Mejoredu/Bases/F911/Ciclo_2023_2024/Finales/Basica/Educación Básica/PREEINDIGENA_I2324.XLSX', sheet_name = 'PREEINDIGENA_I2324')

PRE_I_2 = PRE_I_1.loc[(PRE_I_1['V177'] >= 1)]

PRE_I_2['CCTT'] = PRE_I_2.agg('{0[CV_CCT]}{0[CV_TURNO]}'.format, axis=1)
PRE_I_2['NIVEL'] = '1'
PRE_I_2['MODALIDAD'] = '3'

# Matrícula según edad
PRE_I_2 = PRE_I_2.eval('MAT_EDAESP_H = V122+V123+V124+V897+V139+V140+V900+V151')    
PRE_I_2 = PRE_I_2.eval('MAT_EDAESP_M = V128+V129+V130+V898+V143+V144+V901+V154')    
PRE_I_2 = PRE_I_2.eval('MAT_EDAESP_T = MAT_EDAESP_H+MAT_EDAESP_M')

PRE_I_2 = PRE_I_2.eval('MAT_EDATOT_H = V121+V122+V123+V124+V125+V897+V139+V140+V141+V900+V151+V152')    
PRE_I_2 = PRE_I_2.eval('MAT_EDATOT_M = V127+V128+V129+V130+V131+V898+V143+V144+V145+V901+V154+V155')    
PRE_I_2 = PRE_I_2.eval('MAT_EDATOT_T = MAT_EDATOT_H+MAT_EDATOT_M')

#Seleccionando variables :: .LOC[] permite acceder a las columnas deseadas del DataFrame
PRE_I_3 = PRE_I_2.loc[:, ['CCTT', 'NIVEL', 'MODALIDAD', 
                             'MAT_EDAESP_H', 'MAT_EDAESP_M', 'MAT_EDAESP_T', 
                             'MAT_EDATOT_H', 'MAT_EDATOT_M', 'MAT_EDATOT_T']]   

PRE_I_3.head()
PRE_I_3.shape



##########          COMUNITARIO      
PRE_C_1 = pd.read_excel('C:/Users/raul.guadalupe/Documents/Mejoredu/Bases/F911/Ciclo_2023_2024/Finales/Basica/Educación Básica/Comunitario/PREECOMUNITARIO_I2324.XLSX', sheet_name = 'PREECOMUNITARIO_I2324')

PRE_C_2 = PRE_C_1.loc[(PRE_C_1['V97'] >= 1)]

PRE_C_2['CCTT'] = PRE_C_2.agg('{0[CV_CCT]}{0[CV_TURNO]}'.format, axis=1)
PRE_C_2['NIVEL'] = '1'
PRE_C_2['MODALIDAD'] = '7'

# Matrícula según edad
PRE_C_2 = PRE_C_2.eval('MAT_EDAESP_H = V81+V82+V83')    
PRE_C_2 = PRE_C_2.eval('MAT_EDAESP_M = V87+V88+V89')    
PRE_C_2 = PRE_C_2.eval('MAT_EDAESP_T = MAT_EDAESP_H+MAT_EDAESP_M')

PRE_C_2 = PRE_C_2.eval('MAT_EDATOT_H = V80+V81+V82+V83+V84')    
PRE_C_2 = PRE_C_2.eval('MAT_EDATOT_M = V86+V87+V88+V89+V90')    
PRE_C_2 = PRE_C_2.eval('MAT_EDATOT_T = MAT_EDATOT_H+MAT_EDATOT_M')

#Seleccionando variables :: .LOC[] permite acceder a las columnas deseadas del DataFrame
PRE_C_3 = PRE_C_2.loc[:, ['CCTT', 'NIVEL', 'MODALIDAD', 
                             'MAT_EDAESP_H', 'MAT_EDAESP_M', 'MAT_EDAESP_T', 
                             'MAT_EDATOT_H', 'MAT_EDATOT_M', 'MAT_EDATOT_T']]   

PRE_C_3.head()
PRE_C_3.shape


########## Unión de tablas
PRE = pd.concat([PRE_D_3, PRE_G_3, PRE_I_3, PRE_C_3], axis=0)
print(PRE.head(5))
PRE.shape
PRE.dtypes
PRE.info()



############################################################################################################################
##########          PRIMARIA               ##########

##########          GENERAL      

PRI_G_I1 = pd.read_excel('C:/Users/raul.guadalupe/Documents/Mejoredu/Bases/F911/Ciclo_2023_2024/Finales/Basica/Educación Básica/PRIMGENERAL1_I2324.XLSX', sheet_name = 'PRIMGENERAL1_I2324')
PRI_G_I2 = pd.read_excel('C:/Users/raul.guadalupe/Documents/Mejoredu/Bases/F911/Ciclo_2023_2024/Finales/Basica/Educación Básica/PRIMGENERAL2_I2324.XLSX', sheet_name = 'PRIMGENERAL2_I2324')

PRI_G_1 = pd.merge(PRI_G_I1, PRI_G_I2, on=['CV_CCT','CV_TURNO'], how='inner')

PRI_G_2 = PRI_G_1.loc[(PRI_G_1['V608'] >= 1)]

PRI_G_2['CCTT'] = PRI_G_2.agg('{0[CV_CCT]}{0[CV_TURNO]}'.format, axis=1)
PRI_G_2['NIVEL'] = '2'
PRI_G_2['MODALIDAD'] = '2'

# Matrícula según edad
PRI_G_2 = PRI_G_2.eval('MAT_EDAESP_H = V269+V270+V271+V272+V273+V274+V280+V281+V282+V283+V284+V285+	V326+V327+V328+V329+V330+V331+V337+V338+V339+V340+V341+V342+ V381+V382+V383+V384+V385+V391+V392+V393+V394+V395+	V431+V432+V433+V434+V440+V441+V442+V443+ V476+V477+V478+V484+V485+V486+ V516+V517+V523+V524')    
PRI_G_2 = PRI_G_2.eval('MAT_EDAESP_M = V292+V293+V294+V295+V296+V297+V303+V304+V305+V306+V307+V308+ V348+V349+V350+V351+V352+V353+V359+V360+V361+V362+V363+V364+ V401+V402+V403+V404+V405+V411+V412+V413+V414+V415+ V449+V450+V451+V452+V458+V459+V460+V461+ V492+V493+V494+V500+V501+V502+ V530+V531+V537+V538')    
PRI_G_2 = PRI_G_2.eval('MAT_EDAESP_T = MAT_EDAESP_H+MAT_EDAESP_M')

PRI_G_2 = PRI_G_2.eval('MAT_EDATOT_H = V268+V280+V326+V337+V381+V391+V431+V440+V476+V484+V516+V523+ V269+V281+V327+V338+V382+V392+V432+V441+V477+V485+V517+V524+ V270+V282+V328+V339+V383+V393+V433+V442+V478+V486+V518+V525+ V271+V283+V329+V340+V384+V394+V434+V443+V479+V487+V519+V526+ V272+V284+V330+V341+V385+V395+V435+V444+V480+V488+V520+V527+ V273+V285+V331+V342+V386+V396+V436+V445+V481+V489+V521+V528+ V274+V286+V332+V343+V387+V397+V437+V446+V482+V490+ V275+V287+V333+V344+V388+V398+V438+V447+ V276+V288+V334+V345+V389+V399+ V277+V289+V335+V346+ V278')    
PRI_G_2 = PRI_G_2.eval('MAT_EDATOT_M = V291+V303+V348+V359+V401+V411+V449+V458+V492+V500+V530+V537+ V292+V304+V349+V360+V402+V412+V450+V459+V493+V501+V531+V538+ V293+V305+V350+V361+V403+V413+V451+V460+V494+V502+V532+V539+ V294+V306+V351+V362+V404+V414+V452+V461+V495+V503+V533+V540+ V295+V307+V352+V363+V405+V415+V453+V462+V496+V504+V534+V541+ V296+V308+V353+V364+V406+V416+V454+V463+V497+V505+V535+V542+ V297+V309+V354+V365+V407+V417+V455+V464+V498+V506+ V298+V310+V355+V366+V408+V418+V456+V465+ V299+V311+V356+V367+V409+V419+ V300+V312+V357+V368+ V301')    
PRI_G_2 = PRI_G_2.eval('MAT_EDATOT_T = MAT_EDATOT_H+MAT_EDATOT_M')

#Seleccionando variables :: .LOC[] permite acceder a las columnas deseadas del DataFrame
PRI_G_3 = PRI_G_2.loc[:, ['CCTT', 'NIVEL', 'MODALIDAD', 
                             'MAT_EDAESP_H', 'MAT_EDAESP_M', 'MAT_EDAESP_T', 
                             'MAT_EDATOT_H', 'MAT_EDATOT_M', 'MAT_EDATOT_T']]   

PRI_G_3.head()
PRI_G_3.shape



##########          INDÍGENA      

PRI_I_I1 = pd.read_excel('C:/Users/raul.guadalupe/Documents/Mejoredu/Bases/F911/Ciclo_2023_2024/Finales/Basica/Educación Básica/PRIMINDIGENA1_I2324.XLSX', sheet_name = 'PRIMINDIGENA1_I2324')
PRI_I_I2 = pd.read_excel('C:/Users/raul.guadalupe/Documents/Mejoredu/Bases/F911/Ciclo_2023_2024/Finales/Basica/Educación Básica/PRIMINDIGENA2_I2324.XLSX', sheet_name = 'PRIMINDIGENA2_I2324')

PRI_I_1 = pd.merge(PRI_I_I1, PRI_I_I2, on=['CV_CCT','CV_TURNO'], how='inner')

PRI_I_2 = PRI_I_1.loc[(PRI_I_1['V610'] >= 1)]

PRI_I_2['CCTT'] = PRI_I_2.agg('{0[CV_CCT]}{0[CV_TURNO]}'.format, axis=1)
PRI_I_2['NIVEL'] = '2'
PRI_I_2['MODALIDAD'] = '3'

# Matrícula según edad
PRI_I_2 = PRI_I_2.eval('MAT_EDAESP_H = V271+V272+V273+V274+V275+V276+V282+V283+V284+V285+V286+V287+ V328+V329+V330+V331+V332+V333+V339+V340+V341+V342+V343+V344+ V383+V384+V385+V386+V387+V393+V394+V395+V396+V397+ V433+V434+V435+V436+V442+V443+V444+V445+ V478+V479+V480+V486+V487+V488+ V518+V519+V525+V526')    
PRI_I_2 = PRI_I_2.eval('MAT_EDAESP_M = V294+V295+V296+V297+V298+V299+V305+V306+V307+V308+V309+V310+	V350+V351+V352+V353+V354+V355+V361+V362+V363+V364+V365+V366+ V403+V404+V405+V406+V407+V413+V414+V415+V416+V417+ V451+V452+V453+V454+V460+V461+V462+V463+ V494+V495+V496+V502+V503+V504+ V532+V533+V539+V540')    
PRI_I_2 = PRI_I_2.eval('MAT_EDAESP_T = MAT_EDAESP_H+MAT_EDAESP_M')

PRI_I_2 = PRI_I_2.eval('MAT_EDATOT_H = V270+V282+V328+V339+V383+V393+V433+V442+V478+V486+V518+V525+ V271+V283+V329+V340+V384+V394+V434+V443+V479+V487+V519+V526+ V272+V284+V330+V341+V385+V395+V435+V444+V480+V488+V520+V527+ V273+V285+V331+V342+V386+V396+V436+V445+V481+V489+V521+V528+ V274+V286+V332+V343+V387+V397+V437+V446+V482+V490+V522+V529+ V275+V287+V333+V344+V388+V398+V438+V447+V483+V491+V523+V530+ V276+V288+V334+V345+V389+V399+V439+V448+V484+V492+ V277+V289+V335+V346+V390+V400+V440+V449+ V278+V290+V336+V347+V391+V401+ V279+V291+V337+V348+ V280')    
PRI_I_2 = PRI_I_2.eval('MAT_EDATOT_M = V293+V305+V350+V361+V403+V413+V451+V460+V494+V502+V532+V539+ V294+V306+V351+V362+V404+V414+V452+V461+V495+V503+V533+V540+ V295+V307+V352+V363+V405+V415+V453+V462+V496+V504+V534+V541+ V296+V308+V353+V364+V406+V416+V454+V463+V497+V505+V535+V542+ V297+V309+V354+V365+V407+V417+V455+V464+V498+V506+V536+V543+ V298+V310+V355+V366+V408+V418+V456+V465+V499+V507+V537+V544+ V299+V311+V356+V367+V409+V419+V457+V466+V500+V508+ V300+V312+V357+V368+V410+V420+V458+V467+ V301+V313+V358+V369+V411+V421+ V302+V314+V359+V370+ V303')    
PRI_I_2 = PRI_I_2.eval('MAT_EDATOT_T = MAT_EDATOT_H+MAT_EDATOT_M')

#Seleccionando variables :: .LOC[] permite acceder a las columnas deseadas del DataFrame
PRI_I_3 = PRI_I_2.loc[:, ['CCTT', 'NIVEL', 'MODALIDAD', 
                             'MAT_EDAESP_H', 'MAT_EDAESP_M', 'MAT_EDAESP_T', 
                             'MAT_EDATOT_H', 'MAT_EDATOT_M', 'MAT_EDATOT_T']]   

PRI_I_3.head()
PRI_I_3.shape



##########          COMUNITARIO      

PRI_C_1 = pd.read_excel('C:/Users/raul.guadalupe/Documents/Mejoredu/Bases/F911/Ciclo_2023_2024/Finales/Basica/Educación Básica/Comunitario/PRIMCOMUNITARIO_I2324.XLSX', sheet_name = 'PRIMCOMUNITARIO_I2324')

PRI_C_2 = PRI_C_1.loc[(PRI_C_1['V515'] >= 1)]

PRI_C_2['CCTT'] = PRI_C_2.agg('{0[CV_CCT]}{0[CV_TURNO]}'.format, axis=1)
PRI_C_2['NIVEL'] = '2'
PRI_C_2['MODALIDAD'] = '7'

# Matrícula según edad
PRI_C_2 = PRI_C_2.eval('MAT_EDAESP_H = V176+V177+V178+V179+V180+V181+V187+V188+V189+V190+V191+V192+ V233+V234+V235+V236+V237+V238+V244+V245+V246+V247+V248+V249+ V288+V289+V290+V291+V292+V298+V299+V300+V301+V302+ V338+V339+V340+V341+V347+V348+V349+V350+ V383+V384+V385+V391+V392+V393+ V423+V424+V430+V431')    
PRI_C_2 = PRI_C_2.eval('MAT_EDAESP_M = V199+V200+V201+V202+V203+V204+V210+V211+V212+V213+V214+V215+ V255+V256+V257+V258+V259+V260+V266+V267+V268+V269+V270+V271+ V308+V309+V310+V311+V312+V318+V319+V320+V321+V322+ V356+V357+V358+V359+V365+V366+V367+V368+ V399+V400+V401+V407+V408+V409+ V437+V438+V444+V445')    
PRI_C_2 = PRI_C_2.eval('MAT_EDAESP_T = MAT_EDAESP_H+MAT_EDAESP_M')

PRI_C_2 = PRI_C_2.eval('MAT_EDATOT_H = V175+V187+V233+V244+V288+V298+V338+V347+V383+V391+V423+V430+ V176+V188+V234+V245+V289+V299+V339+V348+V384+V392+V424+V431+ V177+V189+V235+V246+V290+V300+V340+V349+V385+V393+V425+V432+ V178+V190+V236+V247+V291+V301+V341+V350+V386+V394+V426+V433+ V179+V191+V237+V248+V292+V302+V342+V351+V387+V395+V427+V434+ V180+V192+V238+V249+V293+V303+V343+V352+V388+V396+V428+V435+ V181+V193+V239+V250+V294+V304+V344+V353+V389+V397+ V182+V194+V240+V251+V295+V305+V345+V354+ V183+V195+V241+V252+V296+V306+ V184+V196+V242+V253+ V185')    
PRI_C_2 = PRI_C_2.eval('MAT_EDATOT_M = V198+V210+V255+V266+V308+V318+V356+V365+V399+V407+V437+V444+ V199+V211+V256+V267+V309+V319+V357+V366+V400+V408+V438+V445+ V200+V212+V257+V268+V310+V320+V358+V367+V401+V409+V439+V446+ V201+V213+V258+V269+V311+V321+V359+V368+V402+V410+V440+V447+ V202+V214+V259+V270+V312+V322+V360+V369+V403+V411+V441+V448+ V203+V215+V260+V271+V313+V323+V361+V370+V404+V412+V442+V449+ V204+V216+V261+V272+V314+V324+V362+V371+V405+V413+ V205+V217+V262+V273+V315+V325+V363+V372+ V206+V218+V263+V274+V316+V326+ V207+V219+V264+V275+ V208')    
PRI_C_2 = PRI_C_2.eval('MAT_EDATOT_T = MAT_EDATOT_H+MAT_EDATOT_M')

#Seleccionando variables :: .LOC[] permite acceder a las columnas deseadas del DataFrame
PRI_C_3 = PRI_C_2.loc[:, ['CCTT', 'NIVEL', 'MODALIDAD', 
                             'MAT_EDAESP_H', 'MAT_EDAESP_M', 'MAT_EDAESP_T', 
                             'MAT_EDATOT_H', 'MAT_EDATOT_M', 'MAT_EDATOT_T']]   

PRI_C_3.head()
PRI_C_3.shape


########## Unión de tablas
PRI = pd.concat([PRI_G_3, PRI_I_3, PRI_C_3], axis=0)
print(PRI.head(5))
PRI.shape
PRI.dtypes
PRI.info()



############################################################################################################################
##########          SECUNDARIA               ##########

##########          GENERAL      
SEC_G_I1 = pd.read_excel('C:/Users/raul.guadalupe/Documents/Mejoredu/Bases/F911/Ciclo_2023_2024/Finales/Basica/Educación Básica/SECUNDARIA1_I2324.XLSX', sheet_name = 'SECUNDARIA1_I2324')
SEC_G_I2 = pd.read_excel('C:/Users/raul.guadalupe/Documents/Mejoredu/Bases/F911/Ciclo_2023_2024/Finales/Basica/Educación Básica/SECUNDARIA2_I2324.XLSX', sheet_name = 'SECUNDARIA2_I2324')

SEC_G_1 = pd.merge(SEC_G_I1, SEC_G_I2, on=['CV_CCT','CV_TURNO'], how='inner')

SEC_G_2 = SEC_G_1.loc[(SEC_G_1['V340'] >= 1)]

SEC_G_2['CCTT'] = SEC_G_2.agg('{0[CV_CCT]}{0[CV_TURNO]}'.format, axis=1)
SEC_G_2['NIVEL'] = '3'

SEC_G_2.loc[(SEC_G_2['SUBNIVEL'] == 'GENERAL'), 'MODALIDAD'] = '2'                      # General
SEC_G_2.loc[(SEC_G_2['SUBNIVEL'] == 'TÉCNICA'), 'MODALIDAD'] = '4'                      # Técnica
SEC_G_2.loc[(SEC_G_2['SUBNIVEL'] == 'TELESECUNDARIA'), 'MODALIDAD'] = '5'               # Telesecundaria
SEC_G_2.loc[(SEC_G_2['C_CARACTERIZAN2'] == 'PARA TRABAJADORES'), 'MODALIDAD'] = '6'     # Para trabajadores
SEC_G_2.loc[(SEC_G_2['C_CARACTERIZAN2'] == 'MIGRANTE'), 'MODALIDAD'] = '2'              # General (Migrarnte)
SEC_G_2.loc[(SEC_G_2['C_CARACTERIZAN2'] == 'INDIGENA'), 'MODALIDAD'] = '2'              # General (Indígena)

# Matrícula según edad
SEC_G_2 = SEC_G_2.eval('MAT_EDAESP_H = V299+V300+V301+ V307+V308+V309')    
SEC_G_2 = SEC_G_2.eval('MAT_EDAESP_M = V316+V317+V318+ V324+V325+V326')    
SEC_G_2 = SEC_G_2.eval('MAT_EDAESP_T = MAT_EDAESP_H+MAT_EDAESP_M')

SEC_G_2 = SEC_G_2.eval('MAT_EDATOT_H = V306+V314')    
SEC_G_2 = SEC_G_2.eval('MAT_EDATOT_M = V323+V331')    
SEC_G_2 = SEC_G_2.eval('MAT_EDATOT_T = MAT_EDATOT_H+MAT_EDATOT_M')

#Seleccionando variables :: .LOC[] permite acceder a las columnas deseadas del DataFrame
SEC_G_3 = SEC_G_2.loc[:, ['CCTT', 'NIVEL', 'MODALIDAD', 
                             'MAT_EDAESP_H', 'MAT_EDAESP_M', 'MAT_EDAESP_T', 
                             'MAT_EDATOT_H', 'MAT_EDATOT_M', 'MAT_EDATOT_T']]   

SEC_G_3.head()
SEC_G_3.shape

freq01 = SEC_G_3['MODALIDAD'].value_counts() 
print(freq01)
suma1 =  SEC_G_3.groupby('MODALIDAD')[['MAT_EDATOT_T']].sum()
print(suma1)



##########          COMUNITARIO      

SEC_C_1 = pd.read_excel('C:/Users/raul.guadalupe/Documents/Mejoredu/Bases/F911/Ciclo_2023_2024/Finales/Basica/Educación Básica/Comunitario/SECCOMUNITARIO_I2324.XLSX', sheet_name = 'SECCOMUNITARIO_I2324')

SEC_C_2 = SEC_C_1.loc[(SEC_C_1['V257'] >= 1)]

SEC_C_2['CCTT'] = SEC_C_2.agg('{0[CV_CCT]}{0[CV_TURNO]}'.format, axis=1)
SEC_C_2['NIVEL'] = '3'
SEC_C_2['MODALIDAD'] = '7'

# Matrícula según edad
SEC_C_2 = SEC_C_2.eval('MAT_EDAESP_H = V216+V217+V218+ V224+V225+V226')    
SEC_C_2 = SEC_C_2.eval('MAT_EDAESP_M = V233+V234+V235+ V241+V242+V243')    
SEC_C_2 = SEC_C_2.eval('MAT_EDAESP_T = MAT_EDAESP_H+MAT_EDAESP_M')

SEC_C_2 = SEC_C_2.eval('MAT_EDATOT_H = V223+V231')    
SEC_C_2 = SEC_C_2.eval('MAT_EDATOT_M = V240+V248')    
SEC_C_2 = SEC_C_2.eval('MAT_EDATOT_T = MAT_EDATOT_H+MAT_EDATOT_M')

#Seleccionando variables :: .LOC[] permite acceder a las columnas deseadas del DataFrame
SEC_C_3 = SEC_C_2.loc[:, ['CCTT', 'NIVEL', 'MODALIDAD', 
                             'MAT_EDAESP_H', 'MAT_EDAESP_M', 'MAT_EDAESP_T', 
                             'MAT_EDATOT_H', 'MAT_EDATOT_M', 'MAT_EDATOT_T']]   

SEC_C_3.head()
SEC_C_3.shape


########## Unión de tablas
SEC = pd.concat([SEC_G_3, SEC_C_3], axis=0)
print(SEC.head(5))
SEC.shape
SEC.dtypes
SEC.info()



############################################################################################################################
##########          EMS               ##########

##########          BG      
EMS_BG_1 = pd.read_excel('C:/Users/raul.guadalupe/Documents/Mejoredu/Bases/F911/Ciclo_2023_2024/Finales/Media superior/Media Superior/F9117GI_2324.XLSX', sheet_name = 'Resultado1')

#Seleccionando las escuelas que ofrecen preescolar y que tienen matrícula
EMS_BG_2 = EMS_BG_1[EMS_BG_1['C_CARRERA_ESTATUS'].isin(['Activa', 'Liquidacion'])]

# Matrícula según edad
#EMS_BG_2 = EMS_BG_2.eval('MAT_EDAESP_H = V403+V404+V405+V415+V416+V417+ V465+V466+V467+V477+V478+V479+ V525+V526+V536+V537+ V580+V590')    
#EMS_BG_2 = EMS_BG_2.eval('MAT_EDAESP_M = V428+V429+V430+V440+V441+V442+ V489+V490+V491+V501+V502+V503+ V547+V548+V558+V559+ V600+V610')    
EMS_BG_2 = EMS_BG_2.eval('MAT_EDAESP_H = V631+V632+V633 + V643+V644+V645')    
EMS_BG_2 = EMS_BG_2.eval('MAT_EDAESP_M = V656+V657+V658 + V668+V669+V670')    
EMS_BG_2 = EMS_BG_2.eval('MAT_EDAESP_T = MAT_EDAESP_H+MAT_EDAESP_M')

#EMS_BG_2 = EMS_BG_2.eval('MAT_EDATOT_H = V642+V654')    
#EMS_BG_2 = EMS_BG_2.eval('MAT_EDATOT_M = V667+V679')    
EMS_BG_2 = EMS_BG_2.eval('MAT_EDATOT_H = V642+V654')    
EMS_BG_2 = EMS_BG_2.eval('MAT_EDATOT_M = V667+V679')    
EMS_BG_2 = EMS_BG_2.eval('MAT_EDATOT_T = MAT_EDATOT_H+MAT_EDATOT_M')

EMS_BG_2['CCTT'] = EMS_BG_2.agg('{0[CV_CCT]}{0[CV_TURNO]}'.format, axis=1)

freq01 = EMS_BG_2['C_MODALIDAD'].value_counts() 
print(freq01)
EMS_BG_2.shape


##########       Escolarizado        ##########
EMS_BG_ESC_2 = EMS_BG_2[EMS_BG_2['C_MODALIDAD'].isin(['ESCOLARIZADA', 'MIXTA'])]

EMS_BG_ESC_2['NIVEL'] = '5'         # EMS Escolarizado
EMS_BG_ESC_2['MODALIDAD'] = '2'     # BG

EMS_BG_ESC_3 = EMS_BG_ESC_2.loc[:, ['CCTT', 'NIVEL', 'MODALIDAD', 
                             'MAT_EDAESP_H', 'MAT_EDAESP_M', 'MAT_EDAESP_T', 
                             'MAT_EDATOT_H', 'MAT_EDATOT_M', 'MAT_EDATOT_T']]   

EMS_BG_ESC_3.head()
EMS_BG_ESC_3.shape


##########       No Escolarizado        ##########
EMS_BG_NOESC_2 = EMS_BG_2[EMS_BG_2['C_MODALIDAD'].isin(['ESCOLARIZADA', 'MIXTA', 'NO ESCOLARIZADA'])]

EMS_BG_NOESC_2['NIVEL'] = '7'         # EMS No Escolarizado
EMS_BG_NOESC_2['MODALIDAD'] = '2'     # BG

EMS_BG_NOESC_3 = EMS_BG_NOESC_2.loc[:, ['CCTT', 'NIVEL', 'MODALIDAD', 
                             'MAT_EDAESP_H', 'MAT_EDAESP_M', 'MAT_EDAESP_T', 
                             'MAT_EDATOT_H', 'MAT_EDATOT_M', 'MAT_EDATOT_T']]   

EMS_BG_NOESC_3.head()
EMS_BG_NOESC_3.shape



##########          BT      
EMS_BT_1 = pd.read_excel('C:/Users/raul.guadalupe/Documents/Mejoredu/Bases/F911/Ciclo_2023_2024/Finales/Media superior/Media Superior/F9117BTI_2324.XLSX', sheet_name = 'Resultado1')

#Seleccionando las escuelas que ofrecen preescolar y que tienen matrícula
EMS_BT_2 = EMS_BT_1[EMS_BT_1['C_CARRERA_ESTATUS'].isin(['Activa', 'Liquidacion'])]

# Matrícula según edad
#EMS_BT_2 = EMS_BT_2.eval('MAT_EDAESP_H = V478+V479+V480+V490+V491+V492+ V540+V541+V542+V552+V553+V554+ V600+V601+V611+V612+ V655+V665')    
#EMS_BT_2 = EMS_BT_2.eval('MAT_EDAESP_M = V503+V504+V505+V515+V516+V517+ V564+V565+V566+V576+V577+V578+ V622+V623+V633+V634+ V675+V685')    
EMS_BT_2 = EMS_BT_2.eval('MAT_EDAESP_H = V751+V752+V753 + V763+V764+V765')    
EMS_BT_2 = EMS_BT_2.eval('MAT_EDAESP_M = V776+V777+V778 + V788+V789+V790')    
EMS_BT_2 = EMS_BT_2.eval('MAT_EDAESP_T = MAT_EDAESP_H+MAT_EDAESP_M')

#EMS_BT_2 = EMS_BT_2.eval('MAT_EDATOT_H = V762+V774')    
#EMS_BT_2 = EMS_BT_2.eval('MAT_EDATOT_M = V787+V799')    
EMS_BT_2 = EMS_BT_2.eval('MAT_EDATOT_H = V762+V774')    
EMS_BT_2 = EMS_BT_2.eval('MAT_EDATOT_M = V787+V799')    
EMS_BT_2 = EMS_BT_2.eval('MAT_EDATOT_T = MAT_EDATOT_H+MAT_EDATOT_M')

EMS_BT_2['CCTT'] = EMS_BT_2.agg('{0[CV_CCT]}{0[CV_TURNO]}'.format, axis=1)

freq01 = EMS_BT_2['C_MODALIDAD'].value_counts() 
print(freq01)
EMS_BT_2.shape

##########       Escolarizado        ##########
EMS_BT_ESC_2 = EMS_BT_2[EMS_BT_2['C_MODALIDAD'].isin(['ESCOLARIZADA', 'MIXTA'])]

EMS_BT_ESC_2['NIVEL'] = '5'         # EMS Escolarizado
EMS_BT_ESC_2['MODALIDAD'] = '4'     # BT

EMS_BT_ESC_3 = EMS_BT_ESC_2.loc[:, ['CCTT', 'NIVEL', 'MODALIDAD', 
                             'MAT_EDAESP_H', 'MAT_EDAESP_M', 'MAT_EDAESP_T', 
                             'MAT_EDATOT_H', 'MAT_EDATOT_M', 'MAT_EDATOT_T']]   

EMS_BT_ESC_3.head()
EMS_BT_ESC_3.shape


##########       No Escolarizado        ##########
EMS_BT_NOESC_2 = EMS_BT_2[EMS_BT_2['C_MODALIDAD'].isin(['ESCOLARIZADA', 'MIXTA', 'NO ESCOLARIZADA'])]

EMS_BT_NOESC_2['NIVEL'] = '7'         # EMS No Escolarizado
EMS_BT_NOESC_2['MODALIDAD'] = '4'     # BT

EMS_BT_NOESC_3 = EMS_BT_NOESC_2.loc[:, ['CCTT', 'NIVEL', 'MODALIDAD', 
                             'MAT_EDAESP_H', 'MAT_EDAESP_M', 'MAT_EDAESP_T', 
                             'MAT_EDATOT_H', 'MAT_EDATOT_M', 'MAT_EDATOT_T']]   

EMS_BT_NOESC_3.head()
EMS_BT_NOESC_3.shape


########## Unión de tablas
EMS = pd.concat([EMS_BG_ESC_3, EMS_BG_NOESC_3, EMS_BT_ESC_3, EMS_BT_NOESC_3], axis=0)
print(EMS.head(5))
EMS.shape
EMS.dtypes
EMS.info()


suma =  EMS.groupby(['NIVEL', 'MODALIDAD'])[['MAT_EDAESP_T','MAT_EDATOT_T']].sum()
print(suma)

suma =  EMS.groupby(['NIVEL'])[['MAT_EDAESP_T','MAT_EDATOT_T']].sum()
print(suma)


#####       Revisar EMS     #####
EMS['ENT_ADMON'] = EMS['CCTT'].str[:2]

Mat_EMS_Ent = EMS.groupby(['NIVEL', 'ENT_ADMON'])[['MAT_EDAESP_H', 'MAT_EDAESP_M', 'MAT_EDAESP_T', 'MAT_EDATOT_H', 'MAT_EDATOT_M', 'MAT_EDATOT_T']].sum()
print(Mat_EMS_Ent)

####        Salvar la base en Excel
Mat_EMS_Ent.to_excel("C:/Users/raul.guadalupe/Documents/Mejoredu/2025/INMCE/Cobertura/Result/Mat_EMS_Ent.xlsx")  








############################################################################################################################
##########          Integrar todos los niveles y obtener matrículas               ##########

MAT = pd.concat([PRE, PRI, SEC, EMS], axis=0)

suma1 =  MAT.groupby('NIVEL')[['MAT_EDATOT_T']].sum()
print(suma1)

MAT['ENT_ADMON'] = MAT['CCTT'].str[:2]

Mat_Niv_Ent = MAT.groupby(['NIVEL', 'ENT_ADMON'])[['MAT_EDAESP_H', 'MAT_EDAESP_M', 'MAT_EDAESP_T', 'MAT_EDATOT_H', 'MAT_EDATOT_M', 'MAT_EDATOT_T']].sum()
print(Mat_Niv_Ent)

####        Salvar la base en Excel
Mat_Niv_Ent.to_excel("C:/Users/raul.guadalupe/Documents/Mejoredu/2025/INMCE/Cobertura/Result/Mat_Niv_Ent.xlsx")  




############################################################################################################################
##########                  Proyecciones de población                               ##########

POB = pd.read_excel('C:/Users/raul.guadalupe/Documents/Mejoredu/Bases/Conapo/2023/ConDem50a19_ProyPob20a70/0_Pob_Mitad_1950_2070.xlsx')

POB_variables = list(POB.columns.values)
POB_variables

POB_ = POB.loc[(POB['AÑO'] == 2023)]
POB_1 = POB_[POB_['EDAD'].between(3, 18)]

POB_1['POB3_5H'] = POB_1.apply(lambda row: row['POBLACION'] if row['EDAD'] in range(3, 6) and row['SEXO'] == 'Hombres' else None, axis=1)
POB_1['POB3_5M'] = POB_1.apply(lambda row: row['POBLACION'] if row['EDAD'] in range(3, 6) and row['SEXO'] == 'Mujeres' else None, axis=1)
POB_1['POB3_5T'] = POB_1.apply(lambda row: row['POBLACION'] if row['EDAD'] in range(3, 6) else None, axis=1)

POB_1['POB6_11H'] = POB_1.apply(lambda row: row['POBLACION'] if row['EDAD'] in range(6, 12) and row['SEXO'] == 'Hombres' else None, axis=1)
POB_1['POB6_11M'] = POB_1.apply(lambda row: row['POBLACION'] if row['EDAD'] in range(6, 12) and row['SEXO'] == 'Mujeres' else None, axis=1)
POB_1['POB6_11T'] = POB_1.apply(lambda row: row['POBLACION'] if row['EDAD'] in range(6, 12) else None, axis=1)

POB_1['POB12_14H'] = POB_1.apply(lambda row: row['POBLACION'] if row['EDAD'] in range(12, 15) and row['SEXO'] == 'Hombres' else None, axis=1)
POB_1['POB12_14M'] = POB_1.apply(lambda row: row['POBLACION'] if row['EDAD'] in range(12, 15) and row['SEXO'] == 'Mujeres' else None, axis=1)
POB_1['POB12_14T'] = POB_1.apply(lambda row: row['POBLACION'] if row['EDAD'] in range(12, 15) else None, axis=1)

POB_1['POB15_17H'] = POB_1.apply(lambda row: row['POBLACION'] if row['EDAD'] in range(15, 18) and row['SEXO'] == 'Hombres' else None, axis=1)
POB_1['POB15_17M'] = POB_1.apply(lambda row: row['POBLACION'] if row['EDAD'] in range(15, 18) and row['SEXO'] == 'Mujeres' else None, axis=1)
POB_1['POB15_17T'] = POB_1.apply(lambda row: row['POBLACION'] if row['EDAD'] in range(15, 18) else None, axis=1)

POB_1.head()
POB_1.shape

Pob_Eda_Ent = POB_1.groupby(['CVE_GEO'])[['POB3_5H', 'POB3_5M', 'POB3_5T', 'POB6_11H', 'POB6_11M', 'POB6_11T','POB12_14H', 'POB12_14M', 'POB12_14T', 'POB15_17H', 'POB15_17M', 'POB15_17T']].sum()
print(Pob_Eda_Ent)

####        Salvar la base en Excel
Pob_Eda_Ent.to_excel("C:/Users/raul.guadalupe/Documents/Mejoredu/2025/INMCE/Cobertura/Result/Pob_Eda_Ent.xlsx")  


# Para atención en educación inicial 
#pob.loc[(pob['SEXO'] == 'Hombres') & (pob['EDAD'] == 0), 'pobh_o'] = pob['POBLACION']
#pob.head()




