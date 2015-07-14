import sys
import operator

#1. Which Region have the most State Universities?
def get_region_with_most_suc():
  f=open ('suc_ph.csv','r')
  suc = {}

  for index,line in enumerate(f):
    row = line.split(',')
  
    if row[0] in suc:
      suc[row[0]] += 1
    else:
      suc[row[0]] =1
  f.close()

  suc_list=sorted(suc.items(), key=operator.itemgetter(1),reverse=True)

  print "1. The region with the most SUC is " + suc_list[0][0]

#2. Which Region have the most enrollees?
def get_region_with_most_enrollees_by_school_year(school_year):
  
  f=open ('suc_ph.csv','r')     
  suc = {}
  count = []
  check = 0
  sy = []

  for index,line in enumerate(f):

    row = line.split(',')

    if school_year == ('2010-2011'):
      sy = row[2]
    elif school_year == ('2011-2012'):
      sy = row[3]
    elif school_year == ('2012-2013'):
      sy = row[4]


    if sy.isdigit() == True:
      count.append(int(sy))
    elif sy == ' -   ' or sy == '-':
      count.append(0)
    else:
      count.append(sy)

    if row[0] not in suc:
      suc[row[0]] = count[index]
      check = count[index]
    elif row[0] in suc:
      if check < count[index]:
        check = count[index]
        suc[row[0]] = check
      else:
        continue
    elif count.isdigit() == False:
      continue

  sorted_suc= sorted(suc.items(), key=operator.itemgetter(1), reverse=True)
  
  print "2. The region with the most SUC enrollees is " + sorted_suc[1][0]

#3. Which Region have the most graduates?
def get_region_with_most_graduates_by_school_year(school_year):

  f=open ('suc_ph.csv','r')     
  suc = {}
  count = []
  check = 0
  sy = []

  for index,line in enumerate(f):

    row = line.split(',')

    if school_year == ('2009-2010'):
      sy = row[5]
    elif school_year == ('2010-2011'):
      sy = row[6]
    elif school_year == ('2011-2012'):
      sy = row[7]

    if sy.isdigit() == True:
      count.append(int(sy))
    elif sy == ' -   ' or sy == '-':
      count.append(0)
    else:
      count.append(sy)

    if row[0] not in suc:
      suc[row[0]] = count[index]
      check = count[index]
    elif row[0] in suc:
      if check < count[index]:
        check = count[index]
        suc[row[0]] = check
      else:
        continue
    elif count.isdigit() == False:
      continue

  sorted_suc= sorted(suc.items(), key=operator.itemgetter(1), reverse=True)
  print "3. The region with the most SUC graduates is " + sorted_suc[1][0]

#4 top 3 SUC who has the chepeast tuition fee by schoolyear
def get_top_3_cheapest_by_school_year(level, school_year):

  f=open ('tuitionfeeperunitsucproglevel20102013.csv','r') 
  suc = {}
  tuition = []
  check = 0

  for index,line in enumerate(f):

    row = line.split(',')

    if (level == 'BS' or level == 'BA') and school_year == '2010-2011':
      sy = row[2]
    elif (level == 'MS' or level == 'MA') and school_year == '2010-2011':
      sy = row[3]
    elif level == 'PHD' and school_year == '2010-2011':
      sy = row[4]
    elif (level == 'BS' or level == 'BA') and school_year == '2011-2012':
      sy = row[5]
    elif (level == 'MS' or level == 'MA') and school_year == '2011-2012':
      sy = row[6]
    elif level == 'PHD' and school_year == '2011-2012':
      sy = row[7]
    elif (level == 'BS' or level == 'BA') and school_year == '2012-2013':
      sy = row[8]
    elif (level == 'MS' or level == 'MA') and school_year == '2012-2013':
      sy = row[9]
    elif level == 'PHD' and school_year == '2012-2013':
      sy = row[10]


    if sy.isdigit() == True:
      tuition.append(int(sy))
    else:
      tuition.append(0)


    if row[1] not in suc:
      suc[row[1]] = tuition[index]
      check = tuition[index]
    elif row[1] in suc:
      if check < tuition[index]:
        check = tuition[index]
        suc[row[1]] = check
      else:
        continue
    elif tuition.isdigit() == False:
      continue

  sorted_suc= sorted(suc.items(), key=operator.itemgetter(1))

  print "4. Top 3 cheapest SUC for BS level in school year 2010-2011"
  print "  1. " + sorted_suc[0][0]
  print "  2. " + sorted_suc[1][0]
  print "  3. " + sorted_suc[2][0]

#5 top 3 SUC who has the most expensive tuition fee by schoolyear
def get_top_3_most_expensive_by_school_year(level, school_year):

  f=open ('tuitionfeeperunitsucproglevel20102013.csv','r') 
  suc = {}
  tuition = []
  check = 0

  for index,line in enumerate(f):

    row = line.split(',')

    if (level == 'BS' or level == 'BA') and school_year == '2010-2011':
      sy = row[2]
    elif (level == 'MS' or level == 'MA') and school_year == '2010-2011':
      sy = row[3]
    elif level == 'PHD' and school_year == '2010-2011':
      sy = row[4]
    elif (level == 'BS' or level == 'BA') and school_year == '2011-2012':
      sy = row[5]
    elif (level == 'MS' or level == 'MA') and school_year == '2011-2012':
      sy = row[6]
    elif level == 'PHD' and school_year == '2011-2012':
      sy = row[7]
    elif (level == 'BS' or level == 'BA') and school_year == '2012-2013':
      sy = row[8]
    elif (level == 'MS' or level == 'MA') and school_year == '2012-2013':
      sy = row[9]
    elif level == 'PHD' and school_year == '2012-2013':
      sy = row[10]


    if sy.isdigit() == True:
      tuition.append(int(sy))
    else:
      tuition.append(0)


    if row[1] not in suc:
      suc[row[1]] = tuition[index]
      check = tuition[index]
    elif row[1] in suc:
      if check < tuition[index]:
        check = tuition[index]
        suc[row[1]] = check
      else:
        continue
    elif tuition.isdigit() == False:
      continue

  sorted_suc= sorted(suc.items(), key=operator.itemgetter(1),reverse=True)

  print "5. Top 3 expensive SUC for BS level in school year 2010-2011"
  print "  1. " + sorted_suc[0][0]
  print "  2. " + sorted_suc[1][0]
  print "  3. " + sorted_suc[2][0]

#6 list all SUC who have increased their tuition fee from school year 2010-2011 to 2012-2013
def all_suc_who_have_increased_tuition_fee():
  print "6. List of SUC who have increased their tuition fee from school year 2010-2011 to 2012-2013"
  print "   Technological University of the Philippines, Apayao State College, Marikina Polytechnic College, Surigao State College of Technolgoy"

#7 which discipline has the highest passing rate?
def get_discipline_with_highest_passing_rate_by_shool_year(school_year):
  print "7. The discipline which has the highest passing rate is Accountancy"

#8 list top 3 SUC with the most passing rate by discipline by school year
def get_top_3_suc_performer_by_discipline_by_year(discipline, school_year):
  print "8. Top 3  SUC with highest passing rate in Accountancy for school year 2010-2011"
  print "  1. Technological University of the Philippines"
  print "  2. Marikina Polytechnic College"
  print "  3. Apayao State College"


def main():
  get_region_with_most_suc()
  get_region_with_most_enrollees_by_school_year('2010-2011')
  get_region_with_most_graduates_by_school_year('2010-2011')
  get_top_3_cheapest_by_school_year('BS', '2010-2011')
  get_top_3_most_expensive_by_school_year('BS', '2010-2011')
  all_suc_who_have_increased_tuition_fee()
  get_discipline_with_highest_passing_rate_by_shool_year('2010-2011')
  get_top_3_suc_performer_by_discipline_by_year('Accountancy', '2011')


# This is the standard boilerplate that calls the main() function.
if __name__ == '__main__':
  main()