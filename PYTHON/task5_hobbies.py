tennis = {'Evans', 'Stone', 'Roberts', 'Mills', 'Lewis', 'Morgan'}
dota = {'Grant', 'Morgan', 'Evans', 'Mills', 'Jackson', 'Bradley',}
litrball = {'Grant', 'Morgan', 'Evans', 'Gibson', 'Jackson', 'Barlow', 'Adams'}
all_hobbies = tennis & dota & litrball
litrball_dota = (litrball | dota) - tennis
tennis_litrball = (tennis | litrball) - dota
tennis_dota = (tennis | dota) - litrball
only_tennis = (tennis - dota) - litrball
only_dota = (dota - litrball) - tennis
only_litrball = (litrball - tennis) - dota
print("интересуется всем:", all_hobbies, "интересуется всем, кроме тенниса:", litrball_dota, 'интересуется всем, кроме доты:',tennis_litrball,"интересуется всем, кроме литрбола:", tennis_dota,"интересуется только дотой:", only_dota, "интересуется только литрболом:", only_litrball, "интересуется только теннисом:", only_tennis, sep='\n')

