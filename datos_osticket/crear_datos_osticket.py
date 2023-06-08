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
from datetime import datetime

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

    #Condicional por si el mes es febrero, ademas de controlar que el mes y dia no sean menor a 0.
    dias  = 27 if meses == 1 and dias>27 else dias
    dias  = 0 if dias<0 else dias
    meses = 0 if meses<0 else meses
    meses = 11 if meses>11 else meses

    tiempo= str(year)
    tiempo += "-0%s"%(meses+1) if len(str(meses+1))<2 else "-%s"%(meses+1)
    tiempo += "-0%s"%(dias+1) if len(str(dias+1))<2 else "-%s"%(dias+1)
    tiempo += " 0%s"%horas if len(str(horas))<2 else " %s"%horas
    tiempo += ":0%s"%minutos if len(str(minutos))<2 else ":%s"%minutos
    tiempo += ":0%s"%segundos_aux if len(str(segundos_aux))<2 else ":%s"%segundos_aux

    return tiempo

#Funcion que transforma una cadena datetime en segundos
def convertir_datetime_segundos(cadena):
    #1 Año = 31.536.000s; 1 Mes = 2.592.000s; 1 Dia = 86.400s; 1 Hora = 3.600s; 1 Minuto = 60s
    aux_cadena = cadena.split(" ")
    segundos   = 31536000*int(aux_cadena[0].split("-")[0]) + 2592000*(int(aux_cadena[0].split("-")[1])-1) + 86400*(int(aux_cadena[0].split("-")[2])-1)
    segundos  += 3600*int(aux_cadena[1].split(":")[0]) + 60*int(aux_cadena[1].split(":")[1]) + int(aux_cadena[1].split(":")[2])
    return segundos


#Funcion que quita tildes y ñ, de las cadenas que se le entreguen
def quitar_caracteres(cadena):
    aux = cadena.replace("á","a")
    aux = aux.replace("à","a")
    aux = aux.replace("é","e")
    aux = aux.replace("í","i")
    aux = aux.replace("ó","o")
    aux = aux.replace("ú","u")
    aux = aux.replace("ñ","n")

    return aux

numero_agentes  = int(input("Ingresar numero de agentes deseado  : "))
numero_usuarios = int(input("Ingresar numero de usuarios deseado : "))

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


#****LLenado LLenado de la información de agentes a traves de la tabla ost_staff****.

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
    aux_nuevo_agente = ""
    bandera    = 1
    acumulador = 0
    while bandera>0:
        aux_nuevo_agente = "%s_%s"%(nuevo_agente, acumulador)
        acumulador += 1

        if (aux_nuevo_agente in nombres_usuario) == False and (aux_nuevo_agente+"@email.com" in emails) == False:
            bandera = 0
    
    #Se procede a crear las fechas de creacion, actualizacion y ultimo login
    #del usuario al azar entre el periodo actual - 20 años al periodo actual.

    #Se calcula el periodo actual en segundos
    aux_periodo     = datetime.now()
    periodo_actual  = aux_periodo.year*31536000 + (aux_periodo.month-1)*2592000 + (aux_periodo.day-1)*86400
    periodo_actual += aux_periodo.hour*3600 + aux_periodo.minute*60 + aux_periodo.second

    #1 Año = 31.536.000 segundos
    fecha_creacion = random.randint(periodo_actual - 31536000*20, periodo_actual)
    
    #La fecha de actualizacion será una entre la fecha de creacion hasta 4 meses mas, si esque
    #estos cuatro meses no exceden al periodo actual. De lo contrario la fecha actual será el limite.
    fecha_actualizacion = random.randint(fecha_creacion, fecha_creacion + 2592000*4 if fecha_creacion + 2592000*4<periodo_actual else periodo_actual) 

    # Para la ultima fecha de login se toma como referencia la fecha y hora actuales en segundos
    # Y se elige aleatoriamente entre el periodo actual menos 2 dias y el periodo actual.    
    fecha_login = random.randint(periodo_actual- 86400*2, periodo_actual) if fecha_creacion<= periodo_actual- 86400*2 else random.randint(fecha_creacion, periodo_actual)

    #Creacion de una contraseña que por defecto que en verdad no funcionara, debido a que internamente
    #osTicket tiene su codificador y decodificador de contraseñas (Es por esto que en un futuro si se desea
    #entrar a alguna de estas cuestas, primeramente hay que cambiar la contraseña desde osTicket).
    password = "Hola Mundo!!!"
    
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
    #   phone_ext, mobile, signature, isactive, isadmin, isvisible, onvacation,
    #   assigned_only, show_assigned_tickets, change_passwd, max_page_size, auto_refresh_rate, default_signature_type,
    #   default_paper_size, extra, permissions, created, last_login, passwdreset, updated.

    #Pdt: En el caso de un agente bloqueado, en vaciones o administrador he aplicado una probabilidad solo del 17% cuando
    #lo añado en la variable fila_datos debido a que es poco comun que estas dos variables esten en 1.
    agente_activo     = random.choice([1, 1, 1, 1, 1, 0])
    agente_vacaciones = random.choice([0, 0, 0, 0, 0, 1])

    # Si el agente esta de vacaciones pero la actualizacion mas dos meses
    # es menor al periodo actual. Significa que se termino el plazo y se vuelve a 0.
    if agente_vacaciones == 1 and fecha_actualizacion + 2592000*2<periodo_actual:
        agente_vacaciones = 0

    fila_datos = (random.choice(departamentos), random.choice(roles), aux_nuevo_agente,
                  agente.split(" ")[0], agente.split(" ")[1], password,
                  aux_nuevo_agente+"@email.com", numero_telefono,
                  "56", "9%s"%numero_celular, "", agente_activo,
                  random.choice([0, 0, 0, 1]), random.choice([0,1]), agente_vacaciones,
                  random.choice([0,1]), random.choice([0,1]), 0, 0, 0, 'none',
                  'Letter', '{"def_assn_role":true,"browser_lang":"es_ES"}',
                  '{"user.create":1,"user.delete":1,"user.edit":1,"user.manage":1,"user.dir":1,"org.create":1,"org.delete":1,"org.edit":1,"faq.manage":1,"visibility.agents":1,"visibility.departments":1}',
                  convertir_segundos_datetime(fecha_creacion), 
                  # Si el agente esta activo y no está de vacaciones la ultima fecha de login será la prevista
                  # de lo contrario la conexion será 3 dias antes de la fecha de actualizacion
                  convertir_segundos_datetime(fecha_login) if agente_activo==1 and agente_vacaciones==0 else convertir_segundos_datetime(fecha_actualizacion - 86400*3),
                  convertir_segundos_datetime(fecha_creacion),convertir_segundos_datetime(fecha_actualizacion))
    
    sentencia = """INSERT INTO ost_staff(dept_id, role_id, username, firstname, lastname, passwd, email, phone,
                   phone_ext, mobile, signature, isactive, isadmin, isvisible, onvacation,
                   assigned_only, show_assigned_tickets, change_passwd, max_page_size, auto_refresh_rate, default_signature_type,
                   default_paper_size, extra, permissions, created, lastlogin, passwdreset, updated)
                   
                   VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,
                   %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"""

    #Se ejecuta la sentencia y se hace el commit a la base de datos
    cursor = base_datos.cursor()
    cursor.execute(sentencia, fila_datos)
    base_datos.commit()
    cursor.close()
print("Agentes ingresados correctamente...")


#****LLenado de la información de usuarios a traves de la tabla 
#ost_user, ost_user__cdata, ost_user_email, ost_form, 
#ost_form_entry, ost_form_entry_values, ost_form_field ost__search ****.

#Creacion e insercion los datos de usuarios
for usuario in usuarios:
    #Se consulta a bd por los correos de usuarios existentes
    cursor = base_datos.cursor()
    cursor.execute("SELECT address FROM ost_user_email")
    emails = cursor.fetchall()
    emails = [x[0] for x in emails]
    cursor.close()
    
    #Se consulta a bd por los nombres de usuarios existentes
    cursor = base_datos.cursor()
    cursor.execute("SELECT username FROM ost_user_account")
    nombres_usuarios = cursor.fetchall()
    nombres_usuarios = [x[0] for x in nombres_usuarios]
    cursor.close()

    #Se crea un nombre de usuario para el usuario actual
    nuevo_usuario  = usuario.split(" ")[0][0:1].lower()
    nuevo_usuario += usuario.split(" ")[1].lower()
    nuevo_usuario  = quitar_caracteres(nuevo_usuario)

    #Se asigna un numero con el nombre del usuario y se consulta si tal "nombre completo" existe como usuario y como correo
    #si no es asi, este será su nombre de usuario final. Sino el ciclo while sigue con el acumulador incrementado en 1.
    aux_nuevo_usuario = ""
    bandera    = 1
    acumulador = 0
    while bandera>0:
        aux_nuevo_usuario = "%s_%s"%(nuevo_usuario, acumulador)

        if (aux_nuevo_usuario in nombres_usuarios) == False and (aux_nuevo_usuario+"@email.com" in emails) == False:
            bandera = 0
        else:
            acumulador += 1
    
    #Se procede a crear las fechas de creacion y actualizacion
    #del usuario al azar entre el (periodo actual - 20 años) al (periodo actual).

    #Se calcula el periodo actual en segundos
    aux_periodo     = datetime.now()
    periodo_actual  = aux_periodo.year*31536000 + (aux_periodo.month-1)*2592000 + (aux_periodo.day-1)*86400
    periodo_actual += aux_periodo.hour*3600 + aux_periodo.minute*60 + aux_periodo.second

    #1 Año = 31.536.000 segundos
    fecha_creacion      = random.randint(periodo_actual - 31536000*20, periodo_actual)
    fecha_actualizacion = random.randint(fecha_creacion, periodo_actual)

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

    #ORDEN DE DATOS PARA INSERTAR en ost_user_email
    #   user_id (0 momentaneamente), flags (será 0 por defecto), address
    fila_datos = (0, 0 , "%s@email.com"%aux_nuevo_usuario)
    sentencia  = "INSERT INTO ost_user_email(user_id, flags, address) VALUES(%s, %s, %s)"

    #Se insertan los datos en la tabla
    cursor = base_datos.cursor()
    cursor.execute(sentencia, fila_datos)
    base_datos.commit()
    cursor.close()

    #Se consulta a la base de datos por el id del correo que recientemente se ingresó
    cursor = base_datos.cursor()
    cursor.execute("SELECT id FROM ost_user_email WHERE address='%s'"%"%s@email.com"%aux_nuevo_usuario)
    id_correo = cursor.fetchall()[0][0]

    #ORDEN DE DATOS PARA INSERTAR en ost_user
    #   org_id (0 por defecto), default_email_id, status (0 por defecto), name, created, updated
    fila_datos = (0, id_correo, 0, usuario, 
                  convertir_segundos_datetime(fecha_creacion), 
                  convertir_segundos_datetime(fecha_actualizacion))

    sentencia = """INSERT INTO ost_user(org_id, default_email_id, status, name, created, updated) 
                VALUES(%s, %s, %s, %s, %s, %s)"""
    
    cursor = base_datos.cursor()
    cursor.execute(sentencia, fila_datos)
    base_datos.commit()
    cursor.close()

    #Se consulta a la base de datos por el id del usuario que recientemente se ingresó
    cursor = base_datos.cursor()
    cursor.execute("SELECT id FROM ost_user ORDER BY id DESC LIMIT 1")
    id_usuario = cursor.fetchall()[0][0]

    #Se cambia el id de usuario dentro de la tabla de correos
    cursor    = base_datos.cursor()
    sentencia = "UPDATE ost_user_email SET user_id=%s WHERE id=%s"%(id_usuario, id_correo)
    cursor.execute(sentencia)
    base_datos.commit()
    cursor.close()

    #ORDEN DE DATOS PARA INSERTAR en ost_user__cdata
    #   user_id, phone, notes
    fila_datos = (id_usuario, numero_telefono + "X56", "")
    
    #Se insertan los datosen ost_user__cdata
    cursor    = base_datos.cursor()
    sentencia = "INSERT INTO ost_user__cdata(user_id, phone, notes) VALUES(%s, %s, %s)"
    cursor.execute(sentencia, fila_datos)
    base_datos.commit()
    cursor.close()

    #ORDEN DE DATOS PARA INSERTAR en ost_form_entry
    #   form_id (1 por defecto ya que en la tabla ost_form este registro pertenece a un contacto), 
    #   object_id (id del usuario de la tabla ost_user), object_type ("U" por defecto, ya que el registro es un usuario),
    #   sort (1 por defecto), created, updated
    fila_datos = (1, id_usuario, "U", 1, convertir_segundos_datetime(fecha_creacion), convertir_segundos_datetime(fecha_actualizacion))
    sentencia =  "INSERT INTO ost_form_entry(form_id, object_id, object_type, sort, created, updated) VALUES(%s, %s, %s, %s, %s, %s)"
    
    cursor = base_datos.cursor()
    cursor.execute(sentencia, fila_datos)
    base_datos.commit()
    cursor.close()

    #Se consulta a la base de datos por el id del formulario de contacto recientemente creado
    cursor = base_datos.cursor()
    cursor.execute("SELECT id FROM ost_form_entry ORDER BY id DESC LIMIT 1")
    id_formulario = cursor.fetchall()[0][0]
    cursor.close()

    #Se registra el numero telefonico apuntanto al formulario de contacto del usuario en cuestión.
    #ORDEN DE DATOS PARA INSERTAR en ost_form_entry_values
    #   entry_id(id del formulario en la tabla ost_form_entry), 
    #   field_id(por defecto es 3, ya que en la tabla ost_form_field el id 3 equivale a un registro telefonico),
    #   value(aqui se escribe el numero telefonico con la extencion, separados por una "X")

    fila_datos = (id_formulario, 3, numero_telefono+"X56")
    sentencia =  "INSERT INTO ost_form_entry_values(entry_id, field_id, value) VALUES(%s, %s, %s)"
    
    cursor = base_datos.cursor()
    cursor.execute(sentencia, fila_datos)
    base_datos.commit()
    cursor.close()

    #Igualmente se registra que el usuario en cuestión no tiene ninguna nota adicional escrita.
    #Por defecto field_id es 4, debido a que este registro es una nota, pero no hay notas escritas para este usuario.
    fila_datos = (id_formulario, 4)
    cursor = base_datos.cursor()
    cursor.execute("INSERT INTO ost_form_entry_values(entry_id, field_id) VALUES(%s, %s)", fila_datos)
    base_datos.commit()
    cursor.close()

    #ORDEN DE DATOS PARA INSERTAR en ost__search
    #   object_type("U" por defecto, ya que es un usuario), object_id(id del usuario en la tabla ost_user),
    #   title (nombre completo del usuario), content(contiene el numero y el correo separados por espacios)
    fila_datos = ("U", id_usuario, usuario, "%s x56 %s"%(numero_telefono, aux_nuevo_usuario + "@email.com"))
    sentencia =  "INSERT INTO ost__search(object_type, object_id, title, content) VALUES(%s, %s, %s, %s)"
    cursor = base_datos.cursor()
    cursor.execute(sentencia, fila_datos)
    base_datos.commit()
    cursor.close()

    #Se crea una probabilidad del 33% que este nuevo usuario creado esté registrado.
    #Si sale 0, se crea un login para este usuario.
    invitado = [1, 1, 0]

    if random.choice(invitado) == 0:
        #ORDEN DE DATOS PARA INSERTAR en ost_user_account
        #    user_id, status (9 por defecto), timezone ('America/Santiago' por defecto),
        #    username, passwd, registered
        fila_datos = (id_usuario, 9, 'America/Santiago', aux_nuevo_usuario, 'Hola Mundo!!!', convertir_segundos_datetime(fecha_creacion))
        sentencia  = """INSERT INTO ost_user_account(user_id, status, timezone, username, passwd, registered)
                    VALUES(%s, %s, %s, %s, %s, %s)"""
        
        #Se insertan los datos en ost_user_account
        cursor = base_datos.cursor()
        cursor.execute(sentencia, fila_datos)
        base_datos.commit()
        cursor.close()
print("Usuarios ingresados correctamente...")


#****LLenado de la información de tickets a traves de la tabla

#La variable usuarios se convierte en una lista de todos los id de usuarios
#de la base de datos, excepto el usuario con id 1, debido a que este por defecto lo crea osticket.
cursor = base_datos.cursor()
cursor.execute("SELECT id FROM ost_user WHERE id>1")
usuarios = cursor.fetchall()
usuarios = [x[0] for x in usuarios]
cursor.close()

#Se obtienen los ids de departamentos
cursor = base_datos.cursor()
cursor.execute("SELECT id FROM ost_department")
departamentos = cursor.fetchall()
departamentos = [x[0] for x in departamentos]
cursor.close()

#Se obtienen los ids de la tabla ost_help_topic o id de asuntos
cursor = base_datos.cursor()
cursor.execute("SELECT topic_id FROM ost_help_topic")
temas_tickets = cursor.fetchall()
temas_tickets = [x[0] for x in temas_tickets]
cursor.close()

#Se consulta a la tabla ost_ticket_status por los ids de estados y se almacenan en una lista
cursor = base_datos.cursor()
cursor.execute("SELECT id FROM ost_ticket_status ORDER BY id ASC")
estados = cursor.fetchall()
estados = [x[0] for x in estados]
cursor.close()

#Se procede a crear cada unos de los tickets por usuario
for id_usuario in usuarios:
    #Numero de tickets de atención que él usuario habra solicitado.
    cantidad_tickets = random.randint(1,10)

    #Se consulta por la fecha de creación del usuario para despues crear
    #la fecha del ticket utilizando como referencia este periodo en segundos
    cursor = base_datos.cursor()
    cursor.execute("SELECT created FROM ost_user WHERE id='%s'"%id_usuario)
    fecha_creacion_usuario = convertir_datetime_segundos(str(cursor.fetchall()[0][0]))
    cursor.close()

    for ticket in range(0, cantidad_tickets):
        #Se consulta por los numeros de tickets existente
        cursor = base_datos.cursor()
        cursor.execute("SELECT number FROM ost_ticket")
        numeros_tickets_bd = cursor.fetchall()
        numeros_tickets_bd = [int(x[0]) for x in numeros_tickets_bd]
        cursor.close()

        #Se asigna un numero a este nuevo ticket, consultando si este ya existe.
        numero_asignado = 0
        bandera       = 1
        while bandera > 0:
            numero_asignado = random.randint(0,999999)

            if (numero_asignado in numeros_tickets_bd) == False:
                numero_asignado = str(numero_asignado)
                bandera = 0
        
        while len(numero_asignado)<6:
            numero_asignado = "0"+numero_asignado

        # Se elije al azar el departamento al que se asignará el ticket
        id_departamento = random.choice(departamentos)

        # Se procede a consultar por agentes pertenecientes a dado departamento
        # y se crea una lista con sus ids
        cursor = base_datos.cursor()
        cursor.execute("SELECT staff_id FROM ost_staff WHERE dept_id=%s AND isactive=1"%id_departamento)
        aux_agentes_departamento = cursor.fetchall()
        aux_agentes_departamento = [x[0] for x in aux_agentes_departamento]
        cursor.close()

        # Se consulta a la bd cuantos tickets maneja cada agente de dicho departamento de modo que se va a 
        # ordenar la lista desde el agente que tiene menos tickets, hasta el que tiene más
        # y asi distribuir equitativamente la carga de trabajo.
        cursor = base_datos.cursor()
        sentencia = "SELECT staff_id FROM ost_ticket WHERE dept_id=%s GROUP BY staff_id ORDER BY count(*) ASC"%id_departamento
        cursor.execute(sentencia)
        agentes_departamento = cursor.fetchall()
        agentes_departamento = [x[0] for x in agentes_departamento]
        cursor.close()

        # Si un agente de dicho departamento no tiene tickets, no saldrá en la tabla de tickets
        # por eso se añade a la lista ordenada. AL PRINCIPIO, ya que no tiene tickets.
        for x in aux_agentes_departamento:
            if (x in agentes_departamento)== False:
                agentes_departamento = [x] + agentes_departamento

        # Se elimina el 0 de la lista, debido a que no es un agente, solo señala que no
        # está asignado a nadie.
        if 0 in agentes_departamento:
            agentes_departamento.remove(0)

        # Se calcula el periodo actual en segundos
        aux_periodo     = datetime.now()
        periodo_actual  = aux_periodo.year*31536000 + (aux_periodo.month-1)*2592000 + (aux_periodo.day-1)*86400
        periodo_actual += aux_periodo.hour*3600 + aux_periodo.minute*60 + aux_periodo.second
        
        # Se establece la fecha de creación del ticket
        fecha_creacion_ticket = random.randint(fecha_creacion_usuario, periodo_actual)

        # Se establece la fecha limite para la respuesta a este ticket
        fecha_limite_respuesta = fecha_creacion_ticket+ 5*86400

        # Se elije un estado para el ticket actual (Abierto, Cerrado, Archivado, etc)
        estado_asignado = random.choice(estados)

        # Esta variable será un numero binario que señala si el ticket fué contestado o nó.
        # Como factor a destacar hay que considerar que si un ticket sigue abierto
        # es poco probable que lo hayan contestado aún y de lo contrario, si ya está
        # cerrado, archivado o eliminado, es muy probable que lo hayan contestado. 
        # Es por eso que se aplican distintas probabilidades. Si el estado asignado 
        # es 1 (abierto), el ticket tiene una baja probabilidad de que haya sido contestado.
        # al ser distinto de 1 (otros estados como cerrado, archivado, etc), 
        # se da por hecho que se contestó tal ticket.
        contestado = random.choice([0, 0, 0, 0, 0, 1]) if estado_asignado==1 else 1
        
        #Si contestado = 0, el ticket no está contestado la fecha de cierre estará nula
        #Y el agente asignado momentaneamente será el primero de la lista
        fecha_cierre_ticket = None
        agente_asignado     = agentes_departamento[0] if len(agentes_departamento)>0 else 0
        

        if(contestado == 1):
            # La fecha de cierre del ticket muy habitualmente se da dentro del plazo establecido de 5 dias,
            # pero habrán ocaciones en que se exceda este plazo cuando el agente responde, 
            # es por ello que se aplica un 75% de probabilidad de que la respuesta se haya dado dentro del 
            # plazo limite, de lo contrario se puede llegar a retrazar hasta un mes de este plazo, 
            # a esto se debe el choice para el limite de la fecha de cierre que se expone mas adelante.
            aux_cierre = random.choice([fecha_limite_respuesta, 
                                        fecha_limite_respuesta, 
                                        fecha_limite_respuesta, 
                                        fecha_limite_respuesta + 2592000])
            
            #Se asigna una fecha de cierre para este ticket
            fecha_cierre_ticket = random.randint(fecha_creacion_ticket, aux_cierre)

            bandera_agente_encontrado = 0
            contador_agente = 0
            while contador_agente<len(agentes_departamento):
                # Se consulta por la fecha de ultimo login del agente actual, de manera que se compara si
                # este agente accedio en la misma fecha de cerrado o despues, debido a que es ilogico que 
                # alguien que haya resuelto un ticket, no se conectara antes de que este se resolviera.
                # Entonces si este agente cumple esta condicion, se le asigna el ticket. 
                cursor = base_datos.cursor()
                cursor.execute("SELECT lastlogin FROM ost_staff WHERE staff_id='%s'"%agentes_departamento[contador_agente])
                fecha_ultimo_login_agente = convertir_datetime_segundos(str(cursor.fetchall()[0][0]))
                cursor.close()

                #Si efectivamente la fecha de ultimo login es mayor o igual a la fecha de cierre del ticket
                #Se asigna ese agente, si no se cambia a otro.
                if fecha_ultimo_login_agente>=fecha_cierre_ticket:
                    agente_asignado = agentes_departamento[contador_agente]
                    bandera_agente_encontrado = 1
                    contador_agente = len(agentes_departamento)
                else:
                    contador_agente += 1
            
            # Si no se encontró a ningun agente que se haya logueado en la fecha de cierre seleccionada
            # o despues, se cambia el estado del ticket a sin contestar, sin fecha de cierre y de estado
            # abierto.
            if bandera_agente_encontrado == 0:
                contestado = 0
                fecha_cierre_ticket = None
                estado_asignado = 1

        #Se selecciona aleatoriamente el tipo de ticket al que pertenecerá
        tema_asignado = random.choice(temas_tickets)

        #Probabilidad de fuente de conexion
        fuente = ["Web", "Web", "Web", "Web", "Email", "Email", "Phone", "Phone", "API"]

        #ORDEN DE DATOS PARA INSERTAR en ost_ticket
        #    number, user_id, user_email_id (por defecto en 0), status_id, dept_id, sla_id (por defecto 1), topic_id,
        #    staff_id, team_id (0 por defecto), email_id, lock_id (0 por defecto), flags, sort, ip_address,
        #    source, isoverdue, isanswered, est_duedate (fecha limite 5 dias habiles desde la creacion del ticket), closed, lastupdate, 
        #    created, updated
        fila_datos = (numero_asignado, id_usuario, 0, estado_asignado, id_departamento, 1,
                      tema_asignado, agente_asignado, 0, 0, 0, 0, 0, '::1', random.choice(fuente), 
                      #Si la fecha actual es mayor al limite impuesto y ademas este ticket no tiene fecha de cierre
                      #Se considera retrasado. Al igual que si tuviese una fecha de cierre que supera a la fecha impuesta.
                      1 if (fecha_limite_respuesta<periodo_actual and fecha_cierre_ticket==None) or 
                           (fecha_cierre_ticket!=None and fecha_cierre_ticket>fecha_limite_respuesta) else 0, 
                      contestado, convertir_segundos_datetime(fecha_limite_respuesta),
                      convertir_segundos_datetime(fecha_cierre_ticket) if fecha_cierre_ticket!=None else None,
                      convertir_segundos_datetime(fecha_cierre_ticket) if fecha_cierre_ticket!=None else convertir_segundos_datetime(fecha_creacion_ticket),
                      convertir_segundos_datetime(fecha_creacion_ticket), convertir_segundos_datetime(fecha_creacion_ticket))

        #Se procede a insertar los datos en la tabla ost_ticket
        cursor    = base_datos.cursor()
        sentencia = """INSERT INTO ost_ticket(number, user_id, user_email_id, status_id, dept_id, sla_id, topic_id,
                       staff_id, team_id, email_id, lock_id, flags, sort, ip_address, source, isoverdue, isanswered, 
                       est_duedate, closed, lastupdate, created, updated) VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,
                       %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"""
        
        cursor.execute(sentencia, fila_datos)
        base_datos.commit()
        cursor.close()

        #ORDEN DE DATOS PARA INSERTAR en ost_ticket__cdata
        #   ticket_id, subject, priority

        #Se consulta por el id del ticket actual
        cursor = base_datos.cursor()
        cursor.execute("SELECT ticket_id FROM ost_ticket ORDER BY ticket_id DESC LIMIT 1")
        id_ticket_actual = cursor.fetchall()[0][0]
        cursor.close()

        # Se establece la prioridad que tendrá el ticket utilizando como referencia
        # la fecha limite y dependiendo de que tan cerca esté la fecha actual a esa
        # se establece una prioridad u otra. Si no hay fecha de cierre y ya se cumplió
        # el tiempo, la prioridad será de emergencia. 
        # Inicialmente la prioridad sera 0.
        prioridad_ticket = 0

        # Ya que la fecha limite de respuesta representa su fecha de creacion + 5 dias
        # Para la prioridad pense dividir los 5 dias (que estan en segundos) en 3
        # De modo que cada seccion de tiempo represente una prioridad. 
        # Entonces dependiendo si el ticket fue resuelto o no
        # Se compara con estas secciones de tiempo y se determina si la prioridad es 
        # Baja, media, alta o de emergencia.
        secciones_tiempo = (86400*5)/3
        if fecha_cierre_ticket==None:
            if periodo_actual>fecha_limite_respuesta:
                prioridad_ticket = 4
            else:
                aux_fecha_creacion_ticket = fecha_creacion_ticket
                
                bandera = 1
                while bandera>0:
                    aux_fecha_creacion_ticket += secciones_tiempo
                    prioridad_ticket += 1

                    if aux_fecha_creacion_ticket>=fecha_limite_respuesta:
                        bandera = 0
        else:
            if fecha_cierre_ticket > fecha_limite_respuesta:
                prioridad_ticket = 4
            else:
                aux_fecha_creacion_ticket = fecha_creacion_ticket

                bandera = 1
                while bandera>0:
                    aux_fecha_creacion_ticket += secciones_tiempo
                    prioridad_ticket += 1

                    if aux_fecha_creacion_ticket>=fecha_cierre_ticket:
                        bandera = 0

            
        # Se insertan los datos en ost_ticket__cdata
        # Pdt: Para la prioridad es mucho mas probable que sea normal, por lo tanto
        # Se añaden 2 numeradores iguales a 2 (ya que es el id de prioridad normal) y un 1 por prioridad baja.
        asunto_ticket    = "Este es el ticket N°%s"%id_ticket_actual

        fila_datos = (id_ticket_actual, asunto_ticket, prioridad_ticket)
        sentencia  = "INSERT INTO ost_ticket__cdata(ticket_id, subject, priority) VALUES(%s, %s, %s)"

        cursor = base_datos.cursor()
        cursor.execute(sentencia, fila_datos)
        base_datos.commit()
        cursor.close()

        #ORDEN DE DATOS PARA INSERTAR en ost_form_entry
        #    form_id (2 por defecto ya que se trata un ticket), object_id, object_type ("T" por defecto),
        #    sort(0 por defecto), extra('{"disable":[]}' por defecto), created, updated

        cursor = base_datos.cursor()
        fila_datos = (2, id_ticket_actual, "T", 0, '{"disable":[]}',
                      convertir_segundos_datetime(fecha_creacion_ticket),
                      convertir_segundos_datetime(fecha_creacion_ticket))
        sentencia = """ INSERT INTO ost_form_entry(form_id, object_id, object_type, sort, extra, created, updated)
                        VALUES(%s, %s, %s, %s, %s, %s, %s)"""

        #Se insertan los datos
        cursor.execute(sentencia, fila_datos)
        base_datos.commit()
        cursor.close()

        # Se consulta por el id de la conexion hacia el ticket creada anteriormente y se utiliza
        # Para dar la referencia a ost_form_entry_values
        cursor = base_datos.cursor()
        cursor.execute("SELECT id FROM ost_form_entry ORDER BY id DESC LIMIT 1")
        conexion_ticket = cursor.fetchall()[0][0]
        cursor.close()

        #ORDEN DE DATOS PARA INSERTAR en ost_form_entry_values
        #    entry_id, field_id (20, ya que es el asunto), value
        fila_datos = (conexion_ticket, 20, asunto_ticket)
        cursor = base_datos.cursor()
        cursor.execute("""INSERT INTO ost_form_entry_values(entry_id, field_id, value)
                       VALUES(%s, %s, %s)""",fila_datos)
        base_datos.commit()
        cursor.close()

        # Se consulta a la tabla ost_ticket_priority por el valor de la prioridad del actual
        # ticket y asi señalarlo dentro de la tabla ost_form_entry_values
        cursor = base_datos.cursor()
        cursor.execute("SELECT priority_desc FROM ost_ticket_priority WHERE priority_id='%s'"%prioridad_ticket)
        valor_prioridad_ticket = cursor.fetchall()[0][0]
        cursor.close()

        #ORDEN DE DATOS PARA INSERTAR en ost_form_entry_values
        #    entry_id, field_id (22, ya que esta fila señala prioridad del ticket), value, value_id
        fila_datos = (conexion_ticket, 22, valor_prioridad_ticket, prioridad_ticket)
        sentencia = """INSERT INTO ost_form_entry_values(entry_id, field_id, value, value_id)
                       VALUES(%s, %s, %s, %s)"""
        
        #Se insertan los datos en ost_form_entry_values
        cursor = base_datos.cursor()
        cursor.execute(sentencia, fila_datos)
        base_datos.commit()
        cursor.close()

print("Tickets ingresados correctamente.")


# Se preparan los datos para insertarlos en las tablas correspondientes de tareas
cursor = base_datos.cursor()
cursor.execute("SELECT staff_id, dept_id, isactive, created, updated FROM ost_staff WHERE staff_id>1 ORDER BY staff_id ASC")
informacion_agente = cursor.fetchall()
cursor.close()

for agente in informacion_agente:
    n_tareas = random.randint(1, 40)
    contador = 1

    for tarea in range(0, n_tareas):
        # Datos por defecto
        dept_id     = agente[1]
        staff_id    = agente[0]
        object_id   = 0
        object_type = ""
        team_id     = 0
        lock_id     = 0

        cursor = base_datos.cursor()
        cursor.execute("SELECT id FROM ost_task ORDER BY id DESC LIMIT 1")
        ultima_tarea = cursor.fetchall()
        ultima_tarea = ultima_tarea[0][0] if ultima_tarea!=[] else 0 
        cursor.close()

        number = str(ultima_tarea + 1) 
        abierto = random.choice([0, 1])

        #Se calcula el periodo actual en segundos
        aux_periodo     = datetime.now()
        periodo_actual  = aux_periodo.year*31536000 + (aux_periodo.month-1)*2592000 + (aux_periodo.day-1)*86400
        periodo_actual += aux_periodo.hour*3600 + aux_periodo.minute*60 + aux_periodo.second

        # Si el agente está inactivo, las tareas creadas son asignaras dentro del rango en que estuvo activo.
        # de lo contrario solo en una fecha mayor o igual a la creacion del agente hsta la actual
        created = random.randint(convertir_datetime_segundos(str(agente[3])), convertir_datetime_segundos(str(agente[4]))) if agente[2] == 0 else random.randint(convertir_datetime_segundos(str(agente[3])), periodo_actual)
        duedate = created + 2592000
        updated = created if agente[2] == 1 else convertir_datetime_segundos(str(agente[4]))
        
        closed  = None
        if agente[2] == 1:
            closed  = None if abierto == 0 else random.randint(convertir_datetime_segundos(str(agente[3])), periodo_actual)
        
        else:
            closed  = None if abierto == 0 else random.randint(convertir_datetime_segundos(str(agente[3])), convertir_datetime_segundos(str(agente[4])))
        
        # Se insertan los datos en ost_task
        sentencia = """INSERT INTO ost_task(object_id, object_type, number, dept_id, staff_id, team_id, lock_id, flags, duedate, closed, created, updated)
                       VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """
        datos     = (object_id, object_type, number, dept_id, staff_id, team_id, lock_id, 0 if abierto == 1 else 1, convertir_segundos_datetime(duedate), convertir_segundos_datetime(closed) if closed!=None else closed, convertir_segundos_datetime(created), convertir_segundos_datetime(updated))
            
        cursor = base_datos.cursor()
        cursor.execute(sentencia, datos)
        base_datos.commit()
        cursor.close()

        # Se consulta por el id de la tarea recien creada
        cursor = base_datos.cursor()
        cursor.execute("SELECT id FROM ost_task ORDER BY id DESC LIMIT 1")
        task_id = cursor.fetchall()[0][0]
        cursor.close()

        title     = "TAREA %s"%contador
        contador += 1

        # Se inserta el titulo en su tabla correspondiente
        sentencia = "INSERT INTO ost_task__cdata(task_id, title) VALUES(%s, %s)"
        datos     = (task_id, title)

        cursor = base_datos.cursor()
        cursor.execute(sentencia, datos)
        base_datos.commit()
        cursor.close()

        # Se crea el formulario de la actual tarea
        form_id     = 5
        object_id   = task_id
        object_type = "A"
        sort        = 1

        sentencia = """INSERT INTO ost_form_entry(form_id, object_id, object_type, sort, created, updated)
                        VALUES(%s, %s, %s, %s, %s, %s)"""
        
        datos     = (form_id, object_id, object_type, sort, convertir_segundos_datetime(created), convertir_segundos_datetime(updated))

        cursor = base_datos.cursor()
        cursor.execute(sentencia, datos)
        base_datos.commit()
        cursor.close()
        
        # Se consulta por el id de entrada de formulario recien creado
        cursor = base_datos.cursor()
        cursor.execute("SELECT id FROM ost_form_entry ORDER BY id DESC LIMIT 1")
        entry_id = cursor.fetchall()[0][0]
        cursor.close()

        # Se recopilan datos para insertarlos en ost_form_entry_values
        field_id = 32
        value    = title

        sentencia = "INSERT INTO ost_form_entry_values(entry_id, field_id, value) VALUES(%s, %s, %s)"
        datos = (entry_id, field_id, value)

        cursor = base_datos.cursor()
        cursor.execute(sentencia, datos)
        base_datos.commit()
        cursor.close()

        # Se recopilan datos para ser insertados en ost_thread
        datos = (object_id, object_type, convertir_segundos_datetime(created))

        cursor = base_datos.cursor()
        cursor.execute("INSERT INTO ost_thread(object_id, object_type, created) VALUES(%s, %s, %s)", datos)
        base_datos.commit()
        cursor.close()

        # Se consulta por el id de los datos recientemente creados y se asignan para posteriormente utilizarlos
        cursor = base_datos.cursor()
        cursor.execute("SELECT id FROM ost_thread ORDER BY id DESC LIMIT 1")
        thread_id = cursor.fetchall()[0][0]
        cursor.close()

        # Se recopilan datos para ser insertados en la tabla ost_thread_event
        cursor = base_datos.cursor()
        cursor.execute("SELECT username FROM ost_staff WHERE staff_id='%s'"%staff_id)
        username = cursor.fetchall()[0][0]
        cursor.close()

        thread_type = "A"
        event_id    = 1
        team_id     = 0
        topic_id    = 0
        uid         = 1
        uid_type    = "S"
        annulled     = 0
        timestamp   = duedate

        sentencia = """INSERT INTO ost_thread_event(thread_id, thread_type, event_id, staff_id, team_id, dept_id, topic_id, username, uid, uid_type, annulled, timestamp)
                       VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"""
        datos = (thread_id, thread_type, event_id, 0, team_id, dept_id, topic_id, username, uid, uid_type, annulled, timestamp)

        cursor = base_datos.cursor()
        cursor.execute(sentencia, datos)
        base_datos.commit()
        cursor.close()

        # Se inserta el evento de la tarea en esta misma tabla
        event_id = 4
        data = '{"claim":true}'

        sentencia = """INSERT INTO ost_thread_event(thread_id, thread_type, event_id, staff_id, team_id, dept_id, topic_id, username, uid, uid_type, annulled, timestamp, data)
                       VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"""
        datos = (thread_id, thread_type, event_id, staff_id, team_id, dept_id, topic_id, username, uid, uid_type, annulled, timestamp, data)

        cursor = base_datos.cursor()
        cursor.execute(sentencia, datos)
        base_datos.commit()
        cursor.close()

print("Tareas asignadas correctamente.")

        
