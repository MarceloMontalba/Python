# Lista de cursos y sus codigos respectivos que serán ingresados a la base de datos.
cursos = [("PROGRAMACION I", "INFO1120"),
          ("INTRODUCCION A LOS SISTEMAS DE BASE DE DATOS", "INFO1122"), 
          ("PROGRAMACION DE ROBOT", "INFO1139"),
          ("TOPICOS DE MATEMATICA PARA PROGRAMACION", "MAT1102"), 
          ("DESARROLLO DE APLICACIONES CLIENTE SERVIDOR", "INFO1125"),
          ("FISICA", "FIS1102"), 
          ("MANTENCION Y ADMINISTRACION DE SISTEMAS", "INFO1116"), 
          ("PROGRAMACION II", "INFO1123"), 
          ("PROYECTO CRISTIANO, LA VIDA", "IET1412"), 
          ("TALLER DE INTEGRACION I", "INFO1170"), 
          ("ARQUITECTURA DE HARDWARE", "INFO1104"),
          ("INTERCONEXION DE REDES (NETWORKING)", "INFO1103"), 
          ("INTRODUCCION AL DESARROLLO DE APLICAC. EMPRESARIALES", "INFO1127"),
          ("PROGRAMACION III", "INFO1126"), 
          ("PROGRAMACION PARA LA INTEGRACION DE SISTEMAS", "INFO1105"), 
          ("DESARROLLO DE APLICACIONES EMPRESARIALES", "INFO1130"),
          ("INTERFACES DE GRAFICA DE USUARIOS", "INFO1128"), 
          ("LENGUAJE DE MARCADO", "INFO1129"), 
          ("TALLER DE INTEGRACION II", "INFO1171"), 
          ("ANALISIS Y MODELADO DE SOFTWARE", "INFO1131"),
          ("GESTION DE LA INFORMACION (ADM.DE BASE DE DATOS)", "INFO1107"),
          ("INGLES I", "INFO1181"),
          ("INTRODUCCIÓN AL CÁLCULO", "MAT1186"),
          ("TEORIA DE SISTEMAS","INFO1142"),
          ("CALCULO INTERMEDIO","INFO1143"),
          ("DISEÑO DE SOFTWARE","INFO1132"),
          ("INGLES II","INFO1182"),
          ("MICROCONTROLADORES","INFO1106"),
          ("TALLER DE INTEGRACION III","INFO1172"),
          ("CALCULO AVANZADO","INFO1145"),
          ("ETICA PROFESIONAL","IET1431"),
          ("GESTION, ADMINISTRACION Y RR.HH.","INFO1160"),
          ("INGLES III","INFO1183"),
          ("PROYECTOS DE SOFTWARE","INFO1133"),
          ("ELEMENTOS DE ALGEBRA LINEAL PARA LA COMPUTACION","INFO1144"),
          ("EVALUACION DE PROYECTOS. PLAN DE NEGOCIOS","INFO1161"),
          ("SISTEMAS DE COMPUTACION Y PLATAFORMA TECNOLOGICA","INFO1108"),
          ("ASEGURAMIENTO DE LA INFORMACIÓN Y SEGURIDAD","INFO1168"),
          ("INTELIGENCIA ARTIFICIAL","INFO1150"),
          ("PLANIFICACION ESTRATEGICA","INFO1162"),
          ("INTELIGENCIA DE NEGOCIOS","INFO1184"),
          ("TALLER DE INTEGRACION IV","INFO1173"),
          ("TEORIA DE LA COMPUTACION","INFO1148"),
          ("TOPICOS AVANZADOS DE DESARROLLO DE SOFTWARE I","INFO1188"),
          ("TOPICOS AVANZADOS DE DESARROLLO DE SOFTWARE II","INFO1189"),
          ("SIMULACIÓN","INFO1191"),
          ("TALLER DE PREPARACIÓN PARA VIDA LABORAL","INFO1190"),
          ("TOPICO AVANZADO DE DESARROLLO DE SOFTWARE III","INFO1194")]

# Lista de nombres y apellidos que son elegidos al azar para la creacion de usuarios
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

import mysql.connector as mysql, random

# Creacion de categorias
def crear_categorias(n_categorias):
    global base_datos

    cursor    = base_datos.cursor()
    sentencia = "SELECT id FROM mdl_course_categories ORDER BY id DESC LIMIT 1"
    cursor.execute(sentencia)
    ultima_categoria = int(cursor.fetchall()[0][0])
    cursor.close()

    for i in range(ultima_categoria+1, ultima_categoria + 1 +n_categorias):
        name              = "Categoria %s"%i
        descriptionformat = 0
        parent            = 0
        sortorder         = 10000
        coursecount       = 0
        visible           = 1
        visibleold        = 1
        timemodified      = 1685214499
        depth             = 1
        path              = "/%s"%i

        datos = (name, descriptionformat, parent, sortorder, coursecount, visible, visibleold, timemodified, depth, path)
        sentencia = """INSERT INTO mdl_course_categories(name, descriptionformat, parent, sortorder, coursecount, visible,
                       visibleold, timemodified, depth, path) VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"""
        
        cursor = base_datos.cursor()
        cursor.execute(sentencia, datos)
        base_datos.commit()
        cursor.close()

    print("Categorias ingresadas exitosamente.")

# Funcion que crea la información de un curso dada la tupla del mismo.
def crear_datos_curso(tupla_curso):
    global base_datos

    # Datos por defecto.
    fullname          = tupla_curso[0]
    shortname         = tupla_curso[1]
    idnumber          = tupla_curso[1]
    sortorder         = 10000
    summary           = ""
    summaryFormat     = 1
    format            = "topics"
    showgrades        = 1
    newsitems         = 5
    startdate         = 1685246400
    enddate           = 1716782400
    relativedatesmode = 0
    marker            = 0
    maxbytes          = 0
    legacyfiles       = 0
    showreports       = 0
    visible           = 1
    visibleold        = 1
    groupmode         = 0
    groupmodeforce    = 0
    defaultgroupingid = 0
    lang              = ""
    calendarType      = ""
    theme             = ""
    timecreated       = 1685311252
    timemodified      = 1685311252
    requested         = 0
    enablecompletion  = 1
    completionnotify  = 0
    cacherev          = 1685311259

    # Se crea un array de ids de las categorias existentes donde se selecciona una al azar
    cursor = base_datos.cursor()
    cursor.execute("SELECT id FROM mdl_course_categories")
    categories = [x[0] for x in cursor.fetchall()]
    cursor.close()

    # Se procede a insertar los datos creados
    sentencia = """INSERT INTO mdl_course(category, sortorder, fullname, shortname, idnumber, summary, summaryFormat, format,
                   showgrades, newsitems, startdate, enddate, relativedatesmode, marker, maxbytes, legacyfiles, showreports,
                   visible, visibleold, groupmode, groupmodeforce, defaultgroupingid, lang, calendarType, theme, timecreated,
                   timemodified, requested, enablecompletion, completionnotify, cacherev) VALUES(%s, %s, %s, %s, %s, %s,
                   %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"""
    
    datos = (random.choice(categories), sortorder, fullname, shortname, idnumber, summary, summaryFormat, format,
            showgrades, newsitems, startdate, enddate, relativedatesmode, marker, maxbytes, legacyfiles, showreports,
            visible, visibleold, groupmode, groupmodeforce, defaultgroupingid, lang, calendarType, theme, timecreated,
            timemodified, requested, enablecompletion, completionnotify, cacherev)
    
    cursor    = base_datos.cursor()
    cursor.execute(sentencia, datos)
    base_datos.commit()
    cursor.close()

    # Se consulta por el id del curso recien creado para retornar su id
    cursor = base_datos.cursor()
    cursor.execute("SELECT id FROM mdl_course ORDER BY id DESC LIMIT 1")
    id_curso = cursor.fetchall()[0][0]
    cursor.close()

    # Se procede a crear una instancia en la tabla mdl_enrol con el curso recien creado
    enrol           = "manual"
    status          = 0
    courseid        = id_curso
    sortorder       = 0
    enrolperiod     = ""
    enrolstartdate  = 0
    enrolenddate    = 0
    expirynotify    = 0
    expirythreshold = 0
    notifyall       = 0
    roleid          = 5
    timecreated     = 1685646192
    timemodified    = 1685646192

    sentencia = """INSERT INTO mdl_enrol(enrol, status, courseid, sortorder, enrolperiod, enrolstartdate, enrolenddate, 
             expirynotify, expirythreshold, notifyall, roleid, timecreated, timemodified) VALUES(%s, %s, %s, %s, %s, %s, %s,
             %s, %s, %s, %s, %s, %s)"""
    
    datos = (enrol, status, courseid, sortorder, enrolperiod, enrolstartdate, enrolenddate, 
             expirynotify, expirythreshold, notifyall, roleid, timecreated, timemodified)
    
    cursor = base_datos.cursor()
    cursor.execute(sentencia, datos)
    base_datos.commit()
    cursor.close()

    # Se consulta por el id de la instancia de inscripcion recien creada
    cursor = base_datos.cursor()
    cursor.execute("SELECT id FROM mdl_enrol ORDER BY id DESC LIMIT 1")
    id_inscripcion = cursor.fetchall()[0][0]
    cursor.close()

    return (id_curso, id_inscripcion)

# Funcion que quita tildes y ñ, de las cadenas que se le entreguen
def quitar_caracteres(cadena):
    aux = cadena.replace("á","a")
    aux = aux.replace("à","a")
    aux = aux.replace("é","e")
    aux = aux.replace("í","i")
    aux = aux.replace("ó","o")
    aux = aux.replace("ú","u")
    aux = aux.replace("ñ","n")

    return aux

# Creacion de usuarios
def crear_datos_usuario():
    global base_datos

    # Datos por defecto
    auth         = "manual"
    confirmed    = 1
    policyagreed = 1
    deleted      = 0
    suspended    = 0
    mnethostid   = 1
    password     = "Hola Mundo!!!!"
    idnumber     = ""
    emailstop    = 0
    icq          = ""
    skype        = ""
    yahoo        = ""
    aim          = ""
    msn          = ""
    phone1       = ""
    phone2       = ""
    institution  = ""
    department   = ""
    address      = ""
    city         = ""
    country      = "CL"
    lang         = "en"
    calendarType = "gregorian"
    theme        = ""
    timezone     = "America/Santiago"
    firstaccess  = 1685215664
    lastaccess   = 1685395949
    lastlogin    = 1685313119
    currentlogin = 1685380828
    lastip       = "0:0:0:0:0:0:0:1"
    secret       = ""
    picture      = 0
    url          = ""
    description  = ""
    descriptionformat = 1
    mailformat        = 1
    maildigest        = 0
    maildisplay       = 2
    autosubscribe     = 1
    trackforums       = 0
    timecreated       = 1685393525
    timemodified      = 1685393525
    trustbitmask      = 0
    imagealt          = ""
    lastnamephonetic  = ""
    firstnamephonetic = ""
    middlename        = ""
    alternatename     = ""
    moodlenetprofile  = ""

    # Nombres y apellidos asignados al nuevo usuario
    firstname = "%s %s"%(random.choice(nombres_hombres),random.choice(nombres_hombres)) if random.choice([0,1]) == 1 else "%s %s"%(random.choice(nombres_mujeres),random.choice(nombres_mujeres))
    firstname = firstname.upper()
    
    lastname  = "%s %s"%(random.choice(apellidos), random.choice(apellidos))
    lastname  = lastname.upper()

    # Se consulta por los usuarios existentes para generar nombres de usuarios distintos
    cursor = base_datos.cursor()
    cursor.execute("SELECT username FROM mdl_user")
    nombres_usuario = [x[0] for x in cursor.fetchall()]
    cursor.close()
    
    aux_username  = firstname.split(" ")[0][0:1].lower()
    aux_username += lastname.split(" ")[0].lower()
    aux_username  = quitar_caracteres(aux_username)

    username   = ""
    bandera    = 1
    acumulador = 0
    while bandera>0:
        username = "%s_%s"%(aux_username, acumulador)
        acumulador += 1

        if (username in nombres_usuario) == False:
            bandera = 0

    # Se ingresa la información a la base de datos
    sentencia = """ 
            INSERT INTO mdl_user(auth, confirmed, policyagreed, deleted, suspended, mnethostid, password, idnumber, emailstop, icq, 
            skype, yahoo, aim, msn, phone1, phone2, institution, department, address, city, country, lang, calendarType,
            theme, timezone, firstaccess, lastaccess, lastlogin, currentlogin, lastip, secret, picture, url,
            description, descriptionformat, mailformat, maildigest, maildisplay, autosubscribe, trackforums,
            timecreated, timemodified, trustbitmask, imagealt, lastnamephonetic, firstnamephonetic, middlename,
            alternatename, moodlenetprofile, firstname, lastname, username, email) VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s,
            %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,
            %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
    """
    datos = (auth, confirmed, policyagreed, deleted, suspended, mnethostid, password, idnumber, emailstop, icq, 
            skype, yahoo, aim, msn, phone1, phone2, institution, department, address, city, country, lang, calendarType,
            theme, timezone, firstaccess, lastaccess, lastlogin, currentlogin, lastip, secret, picture, url,
            description, descriptionformat, mailformat, maildigest, maildisplay, autosubscribe, trackforums,
            timecreated, timemodified, trustbitmask, imagealt, lastnamephonetic, firstnamephonetic, middlename,
            alternatename, moodlenetprofile, firstname, lastname, username, "%s@email.com"%username)
    
    cursor = base_datos.cursor()
    cursor.execute(sentencia, datos)
    base_datos.commit()
    cursor.close()

#Creacion de contexto de los cursos
def crear_datos_contexto(id_curso):
    global base_datos

    contextlevel = 50
    instanceid   = id_curso
    path         = ""
    depth        = 3
    locked       = 0

    # Se consulta por los paths de contextos existentes para asignar uno unico al contexto actual
    cursor = base_datos.cursor()
    cursor.execute("SELECT path FROM mdl_context ORDER BY path ASC")
    paths  = [x[0] for x in cursor.fetchall()]
    cursor.close()

    ultimo_path = paths[len(paths)-1].split("/")
    contador    = int(ultimo_path[len(ultimo_path)-1])+1
    bandera = 1
    while bandera>0:
        nuevo_path = ""
        for x in range(0, len(ultimo_path)-1):
            nuevo_path += ultimo_path[x]+"/"
        nuevo_path += str(contador)

        if (nuevo_path in paths) == False:
            path = nuevo_path
            bandera = 0
        else:
            contador += 1

    sentencia = """INSERT INTO mdl_context(contextlevel, instanceid, path, depth, locked) VALUES(%s, %s, %s, %s, %s)"""
    datos     = (contextlevel, instanceid, path, depth, locked)
    cursor = base_datos.cursor()
    cursor.execute(sentencia, datos)
    base_datos.commit()
    cursor.close()

    # Se consulta por el id del contexto recien creado para posteriormente retornarlo.
    cursor = base_datos.cursor()
    cursor.execute("SELECT id FROM mdl_context ORDER BY id DESC LIMIT 1")
    id_contexto = cursor.fetchall()[0][0]
    cursor.close()

    return id_contexto

# Asigancion de roles de usuario
def asignar_rol_usuario(id_usuario, id_rol, id_contexto, id_inscripcion):
    global base_datos

    roleid       = id_rol
    contextid    = id_contexto
    userid       = id_usuario
    timemodified = 1685565848
    modifierid   = 2
    component    = ""
    itemid       = 0
    sortorder    = 0

    sentencia = """INSERT INTO mdl_role_assignments(roleid, contextid, userid, timemodified, modifierid, component, 
                   itemid, sortorder) VALUES(%s, %s, %s, %s, %s, %s, %s, %s)"""
    
    datos     = (roleid, contextid, userid, timemodified, modifierid, component, itemid, sortorder)
    cursor    = base_datos.cursor()

    cursor.execute(sentencia, datos)
    base_datos.commit()
    cursor.close()

    # Se procede a inscribir o a matricular al usuario
    status       = 0
    enrolid      = id_inscripcion
    userid       = id_usuario
    timestart    = 1685646199
    timeend      = 0
    modifierid   = 2
    timecreated  = 1685646217
    timemodified = 1685646217

    sentencia = """INSERT INTO mdl_user_enrolments(status, enrolid, userid, timestart, timeend, modifierid, timecreated, timemodified)
                   VALUES(%s, %s, %s, %s, %s, %s, %s, %s)"""
    datos = (status, enrolid, userid, timestart, timeend, modifierid, timecreated, timemodified)

    cursor = base_datos.cursor()
    cursor.execute(sentencia, datos)
    base_datos.commit()
    cursor.close()

# Funcion que crea los topicos de los distintos cursos

# Conexion BD de Moodle
base_datos = mysql.connect(
    host     = "localhost",
    user     = "root",
    password = "",
    database = "moodle",
    port     = "3320"
)

# Se establece aleatoriamente el numero de categorias que se va a crear (entre 1 y 3) y se procede a crearlas.
numero_categorias = random.randint(1, 3)
crear_categorias(numero_categorias)

# Se establece aleatoriamente el numero de usuarios que se va a crear (entre 200 y 300) y se procede a crearlos.
numero_usuarios = random.randint(100, 200)
for i in range(0, numero_usuarios):
    crear_datos_usuario()
print("Usuarios ingresados exitosamente.")


# Seleccion de usuarios que serán profesores y alumnos
cursor    = base_datos.cursor()
cursor.execute("SELECT id FROM mdl_user WHERE id>2")
alumnos = [x[0] for x in cursor.fetchall()]
cursor.close()

# Se establece el numero de usuarios que serán profesores y se agregan a la lista de los mismo,
# para posteriormente eliminarlos de la lista de alumnos.
n_profesores = random.randint(10, 20)
profesores   = []
for i in range(0, n_profesores):
    usuario_elegido = random.choice(alumnos)
    profesores.append(usuario_elegido)
    alumnos.remove(usuario_elegido)

# Se procede a crear un curso y a asignar un profesor y alumnos.
for curso in cursos:
    curso_id, inscripcion_id = crear_datos_curso(curso)
    print("Curso '%s' ingresado correctamente."%curso[0])

    contexto_id = crear_datos_contexto(curso_id)
    print("Contexto del curso '%s' ingresado correctamente."%curso[0])

    # Se asigna aleatoriamente al profesor del curso
    asignar_rol_usuario(random.choice(profesores), 3, contexto_id, inscripcion_id)
    print("Profesor del curso '%s' asignado correctamente."%curso[0])

    # Se genera un numero aleatorio de alumnos (entre 10, 40) que serán 
    # parte del curso y se procede a crearlos
    n_alumnos   = random.randint(10, 40)
    
    # aux_alumnos es una lista auxiliar de usuarios NO REPETIDOS que serán los alumnos del curso
    aux_alumnos = []
    bandera     = 1
    while bandera > 0:
        usuario_elegido = random.choice(alumnos)

        if (usuario_elegido in aux_alumnos) == False:
            aux_alumnos.append(usuario_elegido)

        if len(aux_alumnos) == n_alumnos:
            bandera = 0

    # Se procede a crear a dichos alumnos
    for alumno_id in aux_alumnos:
        asignar_rol_usuario(alumno_id, 5, contexto_id, inscripcion_id)
    print("Alumnos del curso '%s' asignados correctamente."%curso[0])

