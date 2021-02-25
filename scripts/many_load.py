import csv  # https://docs.python.org/3/library/csv.html

# https://django-extensions.readthedocs.io/en/latest/runscript.html

# python3 manage.py runscript many_load

from unesco.models import *
# Unesco_category, Unesco_iso, Unesco_region, Unesco_state, Unesco_site, Membership


def run():
    fhand = open('unesco/load.csv')
    reader = csv.reader(fhand)
    next(reader)  # Advance past the header

    Site.objects.all().delete()
    Category.objects.all().delete()
    State.objects.all().delete()
    Region.objects.all().delete()
    Iso.objects.all().delete()
    
    ind=1
    for row in reader:
        print(ind)
        try:
            y = int(row[3])
        except:
            y = None
        try:
            lo = float(row[4])
        except:
            lo = None
        try:
            la = float(row[5])
        except:
            la = None
        try:
            ar = float(row[6])
        except:
            ar = None
        #if ind == 5 :break
        c, _ = Category.objects.get_or_create(   name         = row[7])
        #print(c, _)
        #print()
        s, _ = State.objects.get_or_create(      name         = row[8])
        #print(s, _)
        #print()
        r, _ = Region.objects.get_or_create(     name         = row[9])
        #print(r, _)
        #print()
        i, _ = Iso.objects.get_or_create(        name         = row[10])
        #print(i, _)
        #print()

        p, _ = Site.objects.get_or_create(       name          = row[0],
                                                 description   = row[1],
                                                 justification = row[2],
                                                 year          = y,
                                                 longitude     = lo,
                                                 latitude      = la,
                                                 area_hectares = ar,
                                                 category = c,
                                                 state =s,
                                                 region = r,
                                                 iso = i)

        p.save()
        ind += 1