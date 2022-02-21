import random
import string
lowercase = "a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"
uppercase = "A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"


def firstName():
    names=('Alexia','Alacia', 'Jordan','John','Andy','Joe','Caroline','Jennifer','Olivia','Anthony','Karen','Linda',
                'Michael','Emanuel','Tiffany','Ashley','Asha','Tony','James','Steffany','Bryan','Ryan', 'Chelsea','Mariah'
                ,'Mariah','Jerrica','Erica','Jerry','Nicole','Arianna','Aria','Rick','Samantha','Samuel','Joseph','Josalyn'
                ,'Darell','Daryl','Matthew','Marcus','Randell','Tyler','Terry','India','Jacob','Benjamin','Ben','Martha',
                'Jayden','Madison','Julian','Hunter','Cameron','Adrian','Evan','Micah','Jasmine','Cierra','Trent','Treya',
                'Xavier','Renee','Paris','Julia','Tory','Lilly','Hannah','Ana','Annah','Martina','Martin','Glenroy',
                'Larry','Jordynn','Toni','Bria','Briana','Bre','Sam','Darylynn','Daria','Jane','Jade','Jae','Ava','Julia',
                'Julie','Eva','Angelina','Adam','Amanda','Ali','Alyssa','Aadi','Katelyn','Peyton','Zahara','Raquel','Chloe',
                'Claire','Charlotte','Carlos','Caleb','Charles','Casey','Charlie','Cabal','Cabe','Cabernet','Daisy',
                'Darren','Diego','Dawn','Daniella','Dick','Damian','Demetria','Ellie','Ethan','Edward','Ezra','Elias',
                'Jaedynn','Camerynn','Abraham','Sean','Eric','Stanley','Markell','Juwann','Mohamad','Curt','Kristian',
                'Lilly','Kayla','Tiffany','Tisha','Tish','Rebecca','Katie','Denisse','Denise','Valerie','Trisha','Melissa',
                'Kim','Kimberly','Sabrina','Tristan','Keenan','Kell','Kristi','Kristan','Kristyn','Kate','Katelyn','Katie',
                'Cheryl','Hart','Valerie','Valorie','Nikki','Cierra','Charlie','Queen','Allen','Kim','Cheryl','Cherlyn',
                'Camal','Kent','Jana','Janet','Janette','Jeanette','Vitaly','Bishop','Sherri','Lori','Gloria','Angela'
                ,'Angie','Angel','Esmeralda','Cindy','Jamie','Steph','Stephanie','Shannon','Ken','Kenn','Aevin','Phukwane'
                'Gonzalez',"Curtis","Leonel","Leo","Leonardo","Ronaldo","Benjamin","Kelsi","Sam","Samantha","Felisha",
                "Kaylin","Jalen","Jaylin","Bradly","Brad","Bradford")
    
    firstName = random.choice(names)
    return firstName

def lastName():
    names=('Johnson','Smith','Williams','Thompson','Friday','Lynch','Baker','Stout','Scott','Tuesday','Perez','Lopez'
            ,'Bryant','Love','Khalid','McKnight','McCurdy','McDonald','Donaldson','Jeffries','Henderson','Wilson',
            'Williams','Brown','Kelly','Turner','Hiotte','Taylor','Mitchell','Burns','Wilson','Avery','Madison','Ryan',
            'Riley','Adison','Parker','Taylor','Stevans','Cape','Lampoe','Austin','Knowles','Curry','Jackson','Hardaway'
            ,'Carson','Reagon','Kai','Kade','Jade','Morgon','Jude','Reese','Dakota','Paxton','Zane','Cane','Janne',
            'Dallas','Skyler','Addison','Cole','Snead','Cook','Purdy','Reid','Ellis','Lane','Laww','Wilkerson',
            'Justice','Notty','Brown','Davis','Miller','Schwartz','McDylan','Morrison','Klein','Mendoza','Sherman',
            'Lawson','Barry','Costa','Nash','Forbes','Jacobs','Duncan','Levine','Hodge','Barry','Wall', 'Figuero',
            'Mendoza','Hancock','Mata','Werner','Stokes','Mccormick','Winters','Mckee','Werner','Costa','Chang',
            'Molina','Huff','Henson','Crane','Wu','Cowan','Hubbard','Rodgers','Berg','Le','Mclean','Porter','Yang',
            'Waller','Limon','Stoute','Stringer','White','Brown','Pepper','Melton','Benson','Camble','Campbell','Bell',
            'Camps','Brenneman','Ramirez','Valdez','Naughtty','Perry','Hill','Carter','Brady','Simpson','Winston',
            'Bishops','Wright','Andriano','Lorell','Ming','Mindingall','Walker','Rousey','Witiker','Bates','Sail',
            'Salles','Small','Smalls','Tate','Tait','Belton','Melton','Nowitski','WerrParker','Miller','Hansen','White',
            'Moore','Nelson','Reade','Read','Reid','Macton','Mixon','Maxton','Mosley','Alpers')

    lastName = random.choice(names)
    return lastName

def address():
    lowercase = "a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"
    uppercase = "A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"
    return

def password():
    chars = string.ascii_uppercase + string.ascii_lowercase + string.digits
    size = random.randint(12, 16)
    password = (''.join(random.choice(chars) for x in range(size)))
    return password


        
