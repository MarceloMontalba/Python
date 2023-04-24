#PROGRAMA PYTHON DE CREACION E INGRESO DE DATOS A LAS DISTINTAS TABLAS DE OSTICKET.

#Lista de nombres de hombres, mujeres y apellidos que son elegidos al azar
nombres_hombres = ['Adel', 'Adonis', 'Ajaz', 'Akos', 'Aldo', 'Amets', 'Amaro',
                    'Aquiles', 'Algimantas', 'Alpidio', 'Amrane', 'Anish', 'Arián',
                    'Ayun', 'Azariel', 'Bagrat', 'Bencomo', 'Bertino', 'Candi',
                    'Cesc', 'Cirino', 'Crisólogo', 'Cruz', 'Danilo', 'Dareck',
                    'Dariel', 'Darin', 'Delmiro', 'Damen', 'Dilan', 'Dipa',
                    'Doménico', 'Drago', 'Edivaldo', 'Elvis', 'Elyan', 'Emeric',
                    'Engracio', 'Ensa', 'Eñaut', 'Eleazar', 'Eros', 'Eufemio',
                    'Feiyang', 'Fiorenzo', 'Foudil', 'Galo', 'Gastón', 'Giulio',
                    'Gautam', 'Gentil', 'Gianni', 'Gianluca', 'Giorgio', 'Gourav',
                    'Grober', 'Guido', 'Guifre', 'Guim', 'Hermes', 'Inge', 'Irai',
                    'Iraitz', 'Iyad', 'Iyán', 'Jeremías', 'Joao', 'Jun', 'Khaled',
                    'Leónidas', 'Lier', 'Lionel', 'Lisandro', 'Lucián', 'Mael',
                    'Misael', 'Moad', 'Munir', 'Nael', 'Najim', 'Neo', 'Neil',
                    'Nikita', 'Nilo', 'Otto', 'Pep', 'Policarpo', 'Radu', 'Ramsés',
                    'Rómulo', 'Roy', 'Severo', 'Sidi', 'Simeón', 'Taha', 'Tao',
                    'Vadim', 'Vincenzo', 'Zaid', 'Zigor', 'Zouhair', 'Hugo', 'Mateo',
                    'Martín', 'Lucas', 'Leo', 'Daniel', 'Alejandro', 'Manuel',
                    'Pablo', 'Álvaro', 'Adrián', 'Enzo', 'Mario', 'Diego', 'David',
                    'Oliver', 'Marcos', 'Thiago', 'Marco', 'Álex', 'Javier', 'Izan',
                    'Bruno', 'Miguel', 'Antonio', 'Gonzalo', 'Liam', 'Gael', 'Marc',
                    'Carlos', 'Juan', 'Ángel', 'Dylan', 'Nicolás', 'José', 'Sergio',
                    'Gabriel', 'Luca', 'Jorge', 'Darío', 'Íker', 'Samuel', 'Eric',
                    'Adam', 'Héctor', 'Francisco', 'Rodrigo', 'Jesús', 'Erik', 'Amir',
                    'Jaime', 'Ian', 'Rubén', 'Aarón', 'Iván', 'Pau', 'Víctor',
                    'Guillermo', 'Luis', 'Mohamed', 'Pedro', 'Julen', 'Unai', 'Rafael',
                    'Santiago', 'Saúl', 'Alberto', 'Noah', 'Aitor', 'Joel', 'Nil', 'Jan',
                    'Pol', 'Raúl', 'Matías', 'Martí', 'Fernando', 'Andrés', 'Rayan',
                    'Alonso', 'Ismael', 'Asier', 'Biel', 'Ander', 'Aleix', 'Axel', 'Alan',
                    'Ignacio', 'Fabio', 'Neizan', 'Jon', 'Teo', 'Isaac', 'Arnau', 'Luka',
                    'Max', 'Imran', 'Youssef', 'Anas', 'Elías', 'Abaigar', 'Adei', 'Adur',
                    'Adiran', 'Aimar', 'Aitor', 'Andoni', 'Ander', 'Antxon', 'Amets',
                    'Aratz', 'Argi', 'Aritz', 'Asier', 'Balkoe', 'Baltz', 'Bazkoare',
                    'Beltso', 'Bernat', 'Beñat', 'Bikendi', 'Biktor', 'Bizen', 'Dabi',
                    'Dari', 'Damen', 'Diagur', 'Dunixi', 'Eako', 'Eder', 'Edorta',
                    'Edur', 'Eki', 'Ekaitz', 'Eladi', 'Elixi', 'Eloi', 'Emiri', 'Eneko',
                    'Endrike', 'Eritz', 'Etor', 'Euken', 'Ferran', 'Frantzisko', 'Ganiz',
                    'Gari', 'Gentzen', 'Gergori', 'Gilem', 'Gizon', 'Goiznabar',
                    'Gontzal', 'Gorka', 'Grazian', 'Guren', 'Haize', 'Haran', 'Haritz',
                    'Heiko', 'Hodei', 'Ibai', 'Ibar', 'Igon', 'Igor', 'Iker', 'Imanol',
                    'Iñaki', 'Ipar', 'Irai', 'Iren', 'Izan', 'Izei', 'Jon', 'Jeino',
                    'Joritz', 'Josu', 'Julen', 'Jurgi', 'Kai', 'Kasi', 'Kauldi', 'Kutun',
                    'Lain', 'Luken', 'Maide', 'Mairu', 'Maren', 'Markel', 'Martitz',
                    'Mikel', 'Negu', 'Neketi', 'Nikanor', 'Odei', 'Oier', 'Oihan',
                    'Orentzi', 'Orixe', 'Ortzadar', 'Ostertz', 'Paken', 'Patxi', 'Roke',
                    'Sanduru', 'Semenko', 'Sendoa', 'Silban', 'Sukil', 'Todor', 'Txarles',
                    'Ugutz', 'Uhaitz', 'Unai', 'Untzalu', 'Urtzi', 'Uztai', 'Xabier',
                    'Zuhaitz', 'Zuri', 'Zuzen', 'Adolf', 'Adrià', 'Agustí', 'Alberic',
                    'Aleix', 'Àlvar', 'Amadeu', 'Andreu', 'Aran', 'Ariel', 'Arnald',
                    'Arnau', 'Artur', 'Bernabe', 'Bernat', 'Biel', 'Blai', 'Carles',
                    'Cesc', 'Climen', 'Constantí', 'Cosme', 'Cristòfol', 'Domènech',
                    'Doroteu', 'Eduard', 'Elies', 'Eloi', 'Elpidi', 'Enric', 'Ernest',
                    'Estanislau', 'Esteve', 'Eugeni', 'Eusevi', 'Feliu', 'Ferran',
                    'Ferrer', 'Fredreric', 'Genari', 'Gener', 'Genis', 'Gonçal', 'Guifré',
                    'Guillem', 'Guiu', 'Honorat', 'Hospici', 'Ignasi', 'Isidre', 'Jacint',
                    'Jan', 'Jaume', 'Joaquín', 'Jonatan', 'Jordi', 'Leopold', 'Lluc',
                    'Marc', 'Marcel', 'Martí', 'Mateu', 'Maurici', 'Màxim', 'Medir',
                    'Moisès', 'Nadal', 'Nicolau', 'Nil', 'Oriol', 'Osvald', 'Ovidi',
                    'Pacomi', 'Pelai', 'Pere', 'Pol', 'Prosper', 'Rafel', 'Raimon',
                    'Raül', 'Ricard', 'Robert', 'Roc', 'Roderic', 'Roger', 'Sanc',
                    'Sàndal', 'Serni', 'Simó', 'Thiago', 'Valentí', 'Vicenç', 'Víctor',
                    'Virgili', 'Xavi', 'Xavier', 'Zoel', 'Agostiño', 'Airas', 'Alberte',
                    'Aleixo', 'Aldán', 'Alexandre', 'Amaro', 'Amil', 'André', 'Anselmo',
                    'Antón', 'Antoín', 'Antoíño', 'Ánxelo', 'Anxo', 'Anxos', 'Artai',
                    'Artur', 'Arximiro', 'Aurelio', 'Basilio', 'Benedito', 'Bento',
                    'Benvito', 'Benxamín', 'Bernal', 'Bernaldo', 'Bernardiño', 'Bieito',
                    'Boaventura', 'Brais', 'Breixo', 'Breogán', 'Brigo', 'Bruno',
                    'Caetano', 'Calisto', 'Calros', 'Camilo', 'Cibrán', 'Cilistro',
                    'Ciriaco', 'Clemenzo', 'Clodio', 'Cosme', 'Cristovo', 'Davide',
                    'Diogo', 'Domingos', 'Duarte', 'Eloy', 'Estevo', 'Euloxio', 'Eutelo',
                    'Euxenio', 'Exidio', 'Fernán', 'Fidel', 'Filipe', 'Firmino', 'Fiz',
                    'Frederico', 'Froitoso', 'Gasparo', 'Goio', 'Hixinio', 'Iago',
                    'Lois', 'Luar', 'Luís', 'Manoel', 'Martiño', 'Odón', 'Pascoal',
                    'Payo', 'Peio', 'Pello', 'Peru', 'Quentin', 'Roi', 'Roxelio', 'Rui',
                    'Tadeu', 'Uxío', 'Vicenzo', 'Virxilio', 'Xabier', 'Xacinto',
                    'Xacobe', 'Xacobo', 'Xaime', 'Xan', 'Xandro', 'Xaneiro', 'Xandre',
                    'Xaquin', 'Xenaro', 'Xeraldo', 'Xerardo', 'Xermán', 'Xesus', 'Xián',
                    'Xoán', 'Xoel', 'Xorxe', 'Xosé', 'Xurxo']
                    
nombres_mujeres = ['Adara', 'Agata', 'Agripina', 'Ainhara', 'Aixa', 'Alegría',
                    'Alia', 'Alla', 'América', 'Aminata', 'Amor', 'Anahí', 'Ania',
                    'Aquilina', 'Ariadne', 'Arya', 'Asia', 'Atenea', 'Bella',
                    'Benilde', 'Camino', 'Carmina', 'Casandra', 'Celina', 'Chaymae',
                    'Clemencia', 'Cora', 'Cruz', 'Custodia', 'Dalila', 'Danae',
                    'Dania', 'Demetria', 'Denise', 'Doina', 'Dominica', 'Dorina',
                    'Doris', 'Duna', 'Elaia', 'Elida', 'Enma', 'Erundina', 'Etelvina',
                    'Evelia', 'Evelin', 'Fatma', 'Federica', 'Flavia', 'Florina',
                    'Gadea', 'Griselda', 'Guacimara', 'Guiomar', 'Hasna', 'Indara',
                    'Inna', 'Iraide', 'Irantzu', 'Ivette', 'Jade', 'Johana', 'Juncal',
                    'Kira', 'Larisa', 'Laureana', 'Leia', 'Lena', 'Leocadia', 'Libe',
                    'Lilia', 'Linda', 'Lisa', 'Liudmila', 'Livia', 'Lluna', 'Luana',
                    'Lucinda', 'Mabel', 'Manar', 'Mariama', 'Marianela', 'Nadine',
                    'Naila', 'Nawal', 'Nazareth', 'Nelly', 'Noah', 'Norah', 'Penélope',
                    'Remei', 'Rosalba', 'Sabah', 'Safia', 'Saliha', 'Saloua', 'Sana',
                    'Sanaa', 'Severina', 'Silvina', 'Talia', 'Tasnim', 'Telma', 'Valle',
                    'Ximena', 'Xiomara', 'Yadira', 'Yamila', 'Yesenia', 'Yuliya',
                    'Yumara', 'Zakia', 'Lucía', 'Sofía', 'Martina', 'María', 'Julia',
                    'Paula', 'Valeria', 'Emma', 'Daniela', 'Carla', 'Alba', 'Noa',
                    'Alma', 'Sara', 'Carmen', 'Vega', 'Lara', 'Mia', 'Valentina',
                    'Olivia', 'Claudia', 'Jimena', 'Lola', 'Chloe', 'Aitana', 'Abril',
                    'Ana', 'Laia', 'Triana', 'Candela', 'Alejandra', 'Elena', 'Vera',
                    'Manuela', 'Adriana', 'Inés', 'Marta', 'Carlota', 'Irene',
                    'Victoria', 'Blanca', 'Marina', 'Laura', 'Rocío', 'Alicia',
                    'Clara', 'Nora', 'Lia', 'Ariadna', 'Zoe', 'Amira', 'Gala', 'Celia',
                    'Leire', 'Eva', 'Ángela', 'Andrea', 'África', 'Luna', 'Ainhoa',
                    'Ainara', 'India', 'Nerea', 'Ona', 'Elsa', 'Isabel', 'Leyre',
                    'Gabriela', 'Aina', 'Cayetana', 'Iria', 'Jana', 'Mar', 'Cloe',
                    'Lina', 'Julieta', 'Adara', 'Naia', 'Iris', 'Nour', 'Mara',
                    'Helena', 'Yasmín', 'Natalia', 'Arlet', 'Diana', 'Aroa', 'Amaia',
                    'Cristina', 'Nahia', 'Isabella', 'Malak', 'Elia', 'Carolina',
                    'Berta', 'Fátima', 'Nuria', 'Azahara', 'Macarena', 'Aurora',
                    'Abantza', 'Abarne', 'Abesti', 'Adartza', 'Adirane', 'Agara',
                    'Agata', 'Agate', 'Aimara', 'Ainara', 'Aines', 'Ainhoa', 'Aintza',
                    'Aintzane.', 'Alaia', 'Alaikari', 'Alaiñe', 'Albane', 'Alda',
                    'Aliza', 'Alize', 'Alode', 'Alodi', 'Aloise', 'Amade', 'Amaia',
                    'Amane', 'Amele', 'Andoitza', 'Ane', 'Antia', 'Anuntxi', 'Arantxa',
                    'Arantza', 'Arene', 'Aretxa', 'Argia', 'Astere', 'Begoña',
                    'Dogartze', 'Domeka', 'Dunixe', 'Ederne', 'Edurne', 'Egia',
                    'Ekaitza', 'Elaia', 'Elaia', 'Elixe', 'Enara', 'Estibaliz',
                    'Eulari', 'Eztia', 'Florentzi', 'Gadea', 'Garaine', 'Gorane',
                    'Gure', 'Haizea', 'Haizeder', 'Hegoa', 'Ibarne', 'Ikerne',
                    'Ilargi', 'Iluntze', 'Iraide', 'Irune', 'Izadi', 'Jaione',
                    'Julene', 'Kaia', 'Kaiene', 'Keltse', 'Kemena', 'Laia', 'Leire',
                    'Letizia', 'Lide', 'Loredi', 'Lukene', 'Lutxi', 'Luzia', 'Maia',
                    'Maitane', 'Maite', 'Malen', 'Markele', 'Mikela', 'Milia',
                    'Mirari', 'Nagore', 'Nahia', 'Nahikari', 'Naiara', 'Naroa',
                    'Nekane', 'Nerea', 'Oihana', 'Oihane', 'Olaia', 'Paule',
                    'Polentze', 'Sabiñe', 'Santsa', 'Sarabe', 'Sua', 'Tala',
                    'Taresa', 'Uda', 'Udane', 'Udara', 'Ula', 'Urzuri', 'Yera',
                    'Zeiane', 'Zohardi', 'Zorione', 'Zumaia', 'Zuria', 'Zuzene',
                    'Abellera', 'Agnès', 'Aida', 'Aïna', 'Aisha', 'Aixa', 'Albà',
                    'Alix', 'Alma', 'Aloma', 'Anaïs', 'Àngels', 'Anna', 'Ares',
                    'Ariadna', 'Arlet', 'Aura', 'Bet', 'Beth', 'Blau', 'Cel',
                    'Cèlia', 'Chloé', 'Cira', 'Clàudia', 'Cloè', 'Consol', 'Cora',
                    'Dàlia', 'Dèlia', 'Dolça', 'Duna', 'Dúnia', 'Edna', 'Elna',
                    'Elsa', 'Emma', 'Estel', 'Etna', 'Finestres', 'Francina',
                    'Gemma', 'Gina', 'Iria', 'Ivet', 'Jana', 'Joana', 'Judit',
                    'Júlia', 'Laia', 'Lara', 'Lea', 'Lena', 'Lia', 'Lis', 'Llora',
                    'Llúcia', 'Margarida', 'Meritxell', 'Mireia', 'Montserrat',
                    'Nàdia', 'Nara', 'Neus', 'Nina', 'Nit', 'Noa', 'Nora', 'Nura',
                    'Núria', 'Ona', 'Queralt', 'Ramona', 'Remei', 'Rita', 'Roser',
                    'Sança', 'Sira', 'Socors', 'Sol', 'Soledat', 'Thaís', 'Txell',
                    'Vera', 'Vinyet', 'Xènia', 'Zoa', 'Ádega', 'Agostiña', 'Áine',
                    'Alana', 'Alborada', 'Albura', 'Alda', 'Aldana', 'Alexandra',
                    'Alexia', 'Alla', 'Alodia', 'Aloia', 'Amaina', 'Amil', 'Antela',
                    'Antía', 'Antoniña', 'Anxa', 'Ánxela', 'Ánxeles', 'Anxélica',
                    'Anxos', 'Apana', 'Aranza', 'Aránzazu', 'Arduína', 'Arxentina',
                    'Asunta', 'Aunia', 'Baia', 'Balla', 'Beata', 'Bélxica', 'Benvida',
                    'Benxamina', 'Branca', 'Brenda', 'Briana', 'Brianda', 'Brisda',
                    'Bríxida', 'Camiño', 'Candea', 'Candeloria', 'Catuxa', 'Cebreiro',
                    'Cecía', 'Cela', 'Celina', 'Celtia', 'Chorima', 'Cía', 'Cilla',
                    'Doa', 'Dubra', 'Einés', 'Elba', 'Elvia', 'Erea', 'Euxea',
                    'Euxenia', 'Evelina', 'Exeria', 'Franqueira', 'Fulxencia',
                    'Glenda', 'Hixinia', 'Icía', 'Ifixenia', 'Ilduara', 'Iria',
                    'Iría', 'Irimia', 'Lana', 'Loucia', 'Malvina', 'Maxina',
                    'Mencía', 'Minia', 'Moira', 'Mor', 'Muma', 'Muriel', 'Navia',
                    'Noela', 'Noreia', 'Roxelia', 'Roxeria', 'Sabela', 'Sarela',
                    'Tareixa', 'Ulla', 'Uxía', 'Virxilia', 'Xacinta', 'Xandra',
                    'Xaquelina', 'Xasmín', 'Xela', 'Xeloíra', 'Xema', 'Xenevra',
                    'Xenia', 'Xenoveva', 'Xenxa', 'Xiana', 'Xilda', 'Xosefa',
                    'Xudite', 'Xulia', 'Xulieta', 'Xunqueira', 'Xuventina', 'Zeltia']

apellidos       = ['González', 'Muñoz', 'Rojas', 'Díaz', 'Pérez', 'Soto',
                    'Contreras', 'Silva', 'Martínez', 'Sepúlveda', 'Morales',
                    'Rodríguez', 'López', 'Fuentes', 'Hernández', 'Torres', 'Araya',
                    'Flores', 'Espinoza', 'Valenzuela', 'Castillo', 'Tapia', 'Reyes',
                    'Gutiérrez', 'Castro', 'Pizarro', 'Álvarez', 'Vásquez', 'Sánchez',
                    'Fernández', 'Ramírez', 'Carrasco', 'Gómez', 'Cortés', 'Herrera',
                    'Núñez', 'Jara', 'Vergara', 'Rivera', 'Figueroa', 'Riquelme',
                    'García', 'Miranda', 'Bravo', 'Vera', 'Molina', 'Vega', 'Campos',
                    'Sandoval', 'Orellana', 'Cárdenas', 'Olivares', 'Alarcón',
                    'Gallardo', 'Ortiz', 'Garrido', 'Salazar', 'Guzmán', 'Henríquez',
                    'Saavedra', 'Navarro', 'Aguilera', 'Parra', 'Romero', 'Aravena',
                    'Vargas', 'Vázquez', 'Cáceres', 'Yáñez', 'Leiva', 'Escobar',
                    'Ruiz', 'Valdés', 'Vidal', 'Salinas', 'Zúñiga', 'Peña', 'Godoy',
                    'Lagos', 'Maldonado', 'Bustos', 'Medina', 'Pino', 'Palma',
                    'Moreno', 'Sanhueza', 'Carvajal', 'Navarrete', 'Sáez', 'Alvarado',
                    'Donoso', 'Poblete', 'Bustamante', 'Toro', 'Ortega', 'Venegas',
                    'Lopez', 'Mendoza', 'Farías', 'San Martín', 'Lucero', 'Sosa',
                    'Quiroga', 'Jiménez', 'Mora', 'Calderón', 'Martín', 'Alonso',
                    'Domínguez', 'Ramos']

import random
import mysql.connector as mysql

#Funcion que quita los decimales de un float sin redondear (Trunca los datos)
def truncar(decimal):
    aux = str(decimal).split(".")
    return int(aux[0])

#Funcion que transforma segundos en cadena formato datetime de mySQL
def convertir_segundos_datetime(segundos):
    #1 Año = 31.536.000s; 1 Mes = 2.592.000s; 1 Dia = 86.400s; 1 Hora = 3.600s; 1 Minuto = 60s
    year         = truncar(segundos/31536000)
    meses        = truncar((segundos - (31536000*year))/2592000)
    dias         = truncar((segundos - (31536000*year) - (2592000 * meses))/86400)
    horas        = truncar((segundos - (31536000 * year) - (2592000 * meses) - (86400 * dias))/3600)
    minutos      = truncar((segundos - (31536000 * year) - (2592000 * meses) - (86400 * dias) - (3600 * horas))/60)
    segundos_aux = segundos - (31536000 * year) - (2592000 * meses) - (86400 * dias) - (3600 * horas) - (60 * minutos)

    #Condicional por si el mes es febrero
    dias = 27 if meses == 1 and dias>27 else dias
    
    datetime = str(year)
    datetime += "-0%s"%(meses+1) if len(str(meses))<2 else "-%s"%(meses+1)
    datetime += "-0%s"%(dias+1) if len(str(dias))<2 else "-%s"%(dias+1)
    datetime += " 0%s"%horas if len(str(horas))<2 else " %s"%horas
    datetime += ":0%s"%minutos if len(str(minutos))<2 else ":%s"%minutos
    datetime += ":0%s"%segundos_aux if len(str(segundos_aux))<2 else ":%s"%segundos_aux

    return datetime

#Funcion que quita tildes y ñ, de las cadenas que se le entreguen
def quitar_caracteres(cadena):
    aux = cadena.replace("á","a")
    aux = aux.replace("é","e")
    aux = aux.replace("í","i")
    aux = aux.replace("ó","o")
    aux = aux.replace("ú","u")
    aux = aux.replace("ñ","n")

    return aux

numero_agentes  = 150
numero_usuarios = 10

agentes  = []
usuarios = []

#Se crean los nombres de los agentes
for i in range(0,numero_agentes):
    bandera = 1
    while bandera > 0 :
        nuevo_nombre  = ""
        nuevo_nombre += random.choice(nombres_hombres) if random.choice([0,1]) == 1 else random.choice(nombres_mujeres)
        nuevo_nombre += " %s"%random.choice(apellidos)

        if (nuevo_nombre in agentes) == False and (nuevo_nombre in usuarios) == False:
            agentes.append(nuevo_nombre)
            bandera = 0

#Se crean los nombres de los usuarios
for i in range(0,numero_usuarios):
    bandera = 1
    while bandera > 0 :
        nuevo_nombre  = ""
        nuevo_nombre += random.choice(nombres_hombres) if random.choice([0,1]) == 1 else random.choice(nombres_mujeres)
        nuevo_nombre += " %s"%random.choice(apellidos)

        if (nuevo_nombre in usuarios) == False and (nuevo_nombre in agentes) == False:
            usuarios.append(nuevo_nombre)
            bandera = 0

#Conexion a la base de datos de osTicket
base_datos = mysql.connect(
    host = "localhost",
    user = "root",
    password = "root",
    database = "osticket"
)

#****LLenado de la tabla ost_staff****.

#Se obtienen los ids de todos los departamentos
cursor = base_datos.cursor()
cursor.execute("SELECT id FROM ost_department")
departamentos = cursor.fetchall()
departamentos = [x[0] for x in departamentos]
cursor.close()

#Se obtienen los ids de todos los roles
cursor = base_datos.cursor()
cursor.execute("SELECT id FROM ost_role")
roles = cursor.fetchall()
roles = [x[0] for x in roles]
cursor.close()

#Creacion e insercion los datos de agentes
for agente in agentes:
    #Se consulta a bd por los nombres de agentes existentes
    cursor = base_datos.cursor()
    cursor.execute("SELECT username FROM ost_staff")
    nombres_usuario = cursor.fetchall()
    nombres_usuario = [x[0] for x in nombres_usuario]
    cursor.close()

    #Se consulta a bd por los correos de agentes existentes
    cursor = base_datos.cursor()
    cursor.execute("SELECT email FROM ost_staff")
    emails = cursor.fetchall()
    emails = [x[0] for x in emails]
    cursor.close()

    #Se crea un nombre de usuario para el agente actual
    nuevo_agente  = agente.split(" ")[0][0:1].lower()
    nuevo_agente += agente.split(" ")[1].lower()
    nuevo_agente  = quitar_caracteres(nuevo_agente)

    #Se asigna un numero con el nombre del agente y se consulta si tal "nombre completo" existe como usuario y como correo
    #si no es asi, este será su nombre de usuario final. Sino el ciclo while sigue con el acumulador incrementado en 1.
    bandera    = 1
    acumulador = 0
    while bandera>0:
        nuevo_agente += "_%s"%acumulador
        acumulador += 1

        if (nuevo_agente in nombres_usuario) == False and (nuevo_agente+"@email.com" in emails) == False:
            bandera = 0
    
    #Se procede a crear las fechas de creacion, actualizacion y ultimo login
    #del usuario al azar entre el año 1997 a 2022 en segundos.
    #1 Año = 31.536.000 segundos
    fecha_creacion      = random.randint(31536000*1997, 31536000*2023)
    fecha_actualizacion = random.randint(fecha_creacion, 31536000*2023)
    fecha_login         = random.randint(31536000*2023, (31536000*2023) + (2592000*3)) if fecha_creacion<= 31536000*2023 else random.randint(fecha_creacion, (31536000*2023) + (2592000*3))

    #Creacion de una contraseña que por defecto será "administrador" que es transformada
    #al se escribe en el metodo de encriptado que usa osTicket.
    password = "$2a$08$2oA0PzcJt8p.WaqLtyGKNe5riWv6TQX9oTQwxust3E92ifWch5GNq"

    #Lista de notas  en la que se elegirá una al azar para el agente
    notas = ["<p><strong>Es un/a buen/a empleado/a! :DD</strong></p>",
             "<p>Gran empleado/a ;)</p>",
             "<p><strong>Empleado/a complicado/a :\</strong></p>"]
    
    #Creacion numero telefonico
    numero_telefono = str(random.randint(0, 99))
    
    if len(numero_telefono)<2:
        numero_telefono = "0%s"%numero_telefono

    aux     = str(random.randint(0, 9999999))
    bandera = 1
    while bandera>0:
        if len(aux)>=7:
            bandera = 0
        else:
            aux = "0" + aux
    
    numero_telefono += aux

    #Creacion numero telefono celular
    numero_celular = str(random.randint(0, 99999999))
    bandera = 1
    while bandera>0:
        if len(numero_celular)>=8:
            bandera = 0
        else:
            numero_celular = "0" + numero_celular

    #ORDEN DE DATOS:
    #   dept_id, role_id, username, firstname, lastname, passwd, email, phone,
    #   phone_ext, mobile, signature, notes, isactive, isadmin, isvisible, onvacation,
    #   assigned_only, show_assigned_tickets, change_passwd, max_page_size, auto_refresh_rate, default_signature_type,
    #   default_paper_size, extra, permissions, created, last_login, passwdreset, updated.

    #Pdt: En el caso de un agente bloqueado o en vaciones he aplicado una probabilidad solo del 17% cuando
    #lo añado en la variable fila_datos debido a que es poco comun que estas dos variables esten en 1.
    fila_datos = (random.choice(departamentos),
                  random.choice(roles),
                  nuevo_agente,
                  agente.split(" ")[0],
                  agente.split(" ")[1],
                  password,
                  nuevo_agente+"@email.com",
                  numero_telefono,
                  "+56",
                  "9%s"%numero_celular,
                  "",
                  random.choice(notas),
                  random.choice([1, 1, 1, 1, 1, 0]),
                  random.choice([0,1]),
                  random.choice([0,1]),
                  random.choice([0, 0, 0, 0, 0, 1]),
                  random.choice([0,1]),
                  random.choice([0,1]),
                  0,
                  0,
                  0,
                  'none',
                  'Letter',
                  '{"def_assn_role":true,"browser_lang":"es_ES"}',
                  '{"user.create":1,"user.delete":1,"user.edit":1,"user.manage":1,"user.dir":1,"org.create":1,"org.delete":1,"org.edit":1,"faq.manage":1,"visibility.agents":1,"visibility.departments":1}',
                  convertir_segundos_datetime(fecha_creacion),
                  convertir_segundos_datetime(fecha_login),
                  convertir_segundos_datetime(fecha_creacion),
                  convertir_segundos_datetime(fecha_actualizacion),
                  )
    
    sentencia = '''INSERT INTO ost_staff(dept_id, role_id, username, firstname, lastname, passwd, email, phone,
                   phone_ext, mobile, signature, notes, isactive, isadmin, isvisible, onvacation,
                   assigned_only, show_assigned_tickets, change_passwd, max_page_size, auto_refresh_rate, default_signature_type,
                   default_paper_size, extra, permissions, created, lastlogin, passwdreset, updated)
                   
                   VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,
                   %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)'''

    #Se ejecuta la sentencia y se hace el commit a la base de datos
    cursor = base_datos.cursor()
    cursor.execute(sentencia, fila_datos)
    base_datos.commit()
    cursor.close()


#****LLenado de la tabla ost__search****. 
#Se almacenan los usuarios en esta tabla si el campo "object_type" = "U"
for usuario in usuarios:
    #Se consulta a la tabla por el campo contenido donde dentro de todo
    #se almacena tambien los correos de usuarios existentes aqui.
    cursor = base_datos.cursor()
    cursor.execute("SELECT object_type, content FROM ost__search")
    contenido = cursor.fetchall()
    emails    = []

    #El campo "content" guarda email, telefono y alguna nota del usuario
    #dependiendo si se agrega una nota o no y el telefono o no, la estructura 
    #del campo content cambia al hacer un split en python.
    for x in contenido:
        if x[0]=="U":
            if len(x[1].split("\n")) == 1:
                emails.append(x[1].split("\n")[0])

            if len(x[1].split("\n")) == 2:
                emails.append(x[1].split("\n")[1]) 

            if len(x[1].split("\n")) == 3:
                emails.append(x[1].split("\n")[2])

    cursor.close()

    #Se crea un correo para el usuario actual
    nuevo_correo  = usuario.split(" ")[0][0:1].lower()
    nuevo_correo += usuario.split(" ")[1].lower()
    nuevo_correo  = quitar_caracteres(nuevo_correo)

    #Se asigna un numero con el correo del usuario y se consulta si tal correo existe
    #si no es asi, este será su correo final. Sino el ciclo while sigue con el acumulador incrementado en 1.
    bandera    = 1
    acumulador = 0
    while bandera>0:
        nuevo_correo += "_%s@email.com"%acumulador
        acumulador   += 1

        if (nuevo_correo in emails) == False:
            bandera = 0
    
    #Lista de notas 
    notas = ["Cliente peligroso", "Buen Cliente", "Tranquilo"]

    #Creacion numero telefonico
    numero_telefono = "%s"%random.randint(0, 99)
    
    if len(numero_telefono)<2:
        numero_telefono = "0%s"%numero_telefono

    aux     = str(random.randint(0, 9999999))
    bandera = 1
    while bandera>0:
        if len(aux)>=7:
            bandera = 0
        else:
            aux = "0"+aux

    numero_telefono += aux + " x56"

    #Se consulta por los ids de tipo usuario para no asignar uno existente
    cursor = base_datos.cursor()
    cursor.execute("SELECT object_id FROM ost__search WHERE object_type='U'")
    codigos = cursor.fetchall()
    codigos = [x[0] for x in codigos]
    cursor.close()
    
    #El acumulador sera utilizado como el id del nuevo usuario.
    #Si este ya existe se procede a aumentarlo en 1 hasta que encuentre un id que aun no haya sido creado.
    acumulador = 0
    bandera    = 1
    while(bandera>0):
        fila_datos = (
            "U",
            acumulador,
            usuario,
            "%s\n%s\n%s"%(numero_telefono, random.choice(notas), nuevo_correo)
        )

        if (acumulador in codigos) == False and acumulador!=0:
            #ORDEN DE DATOS:
            #   object_type, object_id, title, content
            sentencia = "INSERT INTO ost__search(object_type, object_id, title, content) VALUES(%s,%s,%s,%s)"

            cursor = base_datos.cursor()
            cursor.execute(sentencia, fila_datos)
            base_datos.commit()
            cursor.close()

            bandera = 0
        
        else:
            acumulador+= 1