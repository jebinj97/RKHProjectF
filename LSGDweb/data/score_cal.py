from .models import Aadhar, User, Accessibility, FamilyIncome, Availability, Transportation, CurrentHealth, \
    MedicalAccessibility, Land, CurrentlyResiding, Credits


def get_education(age, dist, electricity, studyroom, income, computer, smartphone, internet,
                  vehicles, publictrans, caste):
    score = 0
    # age consideration
    if age < 19:
        score = score + 1 * 1.5
    elif age > 18 & age < 26:
        score = score + 3 * 1.5
    elif age > 25 & age < 36:
        score = score + 4 * 1.5
    elif age > 35 & age < 51:
        score = score + 8 * 1.5
    else:
        score = score + 10 * 1.5
    # distance consideration
    if dist < 4:
        score = score + 10 * 0.8
    elif dist > 3 & dist < 5:
        score = score + 8 * 0.8
    elif dist > 5 & dist < 9.1:
        score = score + 3 * 0.8
    else:
        score = score + 0
    # electricity consideration
    if electricity < 4:
        score = score + 0
    elif electricity > 3 & electricity < 11:
        score = score + 1 * 1.5
    elif electricity > 10 & electricity < 17:
        score = score + 3 * 1.5
    else:
        score = score + 9 * 1.5
    # study room consideration
    if studyroom.upper() == 'YES':
        score = score + 10 * 0.4
    # income consideration
    if income < 50001:
        score = score + 0
    elif income > 50000 & income < 100001:
        score = score + 1 * 2.4
    elif income > 100000 & income < 300001:
        score = score + 3 * 2.4
    elif income > 300000 & income < 600001:
        score = score + 5 * 2.4
    elif income > 600000 & income < 120001:
        score = score + 8 * 2.4
    else:
        score = score + 10 * 2.4
    # computers consideration
    if computer == 0:
        score = score + 0
    elif computer == 1:
        score = score + 6 * 0.4
    elif computer == 2:
        score = score + 9 * 0.4
    else:
        score = score + 10 * 0.4
    # smartphone consideration
    if smartphone == 0:
        score = score + 0
    elif smartphone == 1:
        score = score + 2 * 0.4
    elif smartphone == 2:
        score = score + 4 * 0.4
    elif smartphone == 3:
        score = score + 5 * 0.4
    else:
        score = score + 9 * 0.4
    # internet consideration
    if internet.upper() == 'YES':
        score = score + 10 * 0.4
    # vehicle considerations
    if vehicles == 0:
        score = score + 0
    elif vehicles == 1:
        score = score + 7 * 0.6
    else:
        score = score + 10 * 0.6
    # public transport consideration
    if publictrans < 4:
        score = score + 1 * 0.6
    elif publictrans > 3 & publictrans < 7:
        score = score + 3 * 0.6
    elif publictrans > 6 & publictrans < 11:
        score = score + 4 * 0.6
    elif publictrans > 10 & publictrans < 20:
        score = score + 7 * 0.6
    else:
        score = score + 10 * 0.6
    # caste consideration
    if caste.upper() == 'GEN':
        score = score + 10
    elif caste.upper() == 'OBC':
        score = score + 7
    elif caste.upper() == 'SC' or caste.upper() == 'ST':
        score = score + 3
    return score


def get_medical(issues, dist_hospital, fourwheels, dist_pharmacy, income, assestvalue, healtaids, disability,
                insurance, ):
    score = 0
    if issues > 2:
        score = score + 0
    elif issues == 1:
        score = score + 3 * 1.5
    elif issues == 0:
        score = score + 10 * 1.5
    # nearest hospital consideration
    if dist_hospital < 4:
        score = score + 10 * 0.6
    elif dist_hospital > 3 & dist_hospital < 6:
        score = score + 5 * 0.6
    elif dist_hospital > 5 & dist_hospital < 11:
        score = score + 1 * 0.6
    else:
        score = score + 0
    # four wheeler availability consideration
    if fourwheels == 0:
        score = score + 0
    else:
        score = score + 10 * 0.3
    # nearest pharmacy availability consideration
    if dist_pharmacy < 4:
        score = score + 10 * 0.3
    elif dist_pharmacy > 3 & dist_pharmacy < 6:
        score = score + 7 * 0.3
    elif dist_pharmacy > 5 & dist_pharmacy < 11:
        score = score + 3 * 0.3
    else:
        score = score + 0
    # income consideration
    if income < 50001:
        score = score + 0
    elif income > 50000 & income < 100001:
        score = score + 1 * 3
    elif income > 100000 & income < 300001:
        score = score + 2 * 3
    elif income > 300000 & income < 600001:
        score = score + 4 * 3
    elif income > 600000 & income < 1200001:
        score = score + 6 * 3
    else:
        score = score + 10 * 3
    # assest value consideration
    if assestvalue < 100001:
        score = score + 0
    elif assestvalue > 100000 & assestvalue < 300001:
        score = score + 2 * 1.8
    elif assestvalue > 300000 & assestvalue < 800001:
        score = score + 5 * 1.8
    elif assestvalue > 800000 & assestvalue < 1500001:
        score = score + 8 * 1.8
    else:
        score = score + 10 * 1.8
    # existing health aids considerations
    if healtaids == 0:
        score = score + 0
    elif healtaids == 1:
        score = score + 1 * 0.5
    elif healtaids == 2:
        score = score + 3 * 0.5
    elif healtaids >= 3:
        score = score + 7 * 0.5
    # disability consideration
    if disability.upper() == 'YES':
        score = score + 0
    else:
        score = score + 10*1.3
    # medical insurance consideration
    if insurance < 100001:
        score = score + 0
    elif insurance > 100000 & insurance < 300001:
        score = score + 2 * 0.6
    elif insurance > 300000 & insurance < 500001:
        score = score + 4 * 0.6
    elif insurance > 500000 & insurance < 1000001:
        score = score + 7 * 0.6
    else:
        score = score + 10 * 0.6
    return score


def get_land(agland, acland, valueposses):
    score = 0
    # agricultural land considerations
    if agland <= 2:
        score = score + 0
    elif agland > 2 & agland <= 10:
        score = score + 2 * 5
    elif agland > 10 & agland <= 100:
        score = score + 6 * 5
    else:
        score = score + 10 * 5
    # ancestral land consideration
    if acland <= 2:
        score = score + 0
    elif acland > 2 & acland <= 5:
        score = score + 4 * 3
    elif acland > 5 & acland <= 8:
        score = score + 6 * 3
    elif acland > 8 & acland <= 15:
        score = score + 8 * 3
    else:
        score = score + 10 * 3
    # total value of possession considerations
    if valueposses <= 100000:
        score = score + 0
    elif valueposses > 100000 & valueposses <= 300000:
        score = score + 1 * 2
    elif valueposses > 300000 & valueposses <= 700000:
        score = score + 3 * 2
    elif valueposses > 700000 & valueposses <= 1500000:
        score = score + 6 * 2
    elif valueposses > 1500000 & valueposses <= 2500000:
        score = score + 8 * 2
    else:
        score = score + 10 * 2

    return score


def get_house(ownership, members, area, water, roofing,
              bathrooms, electricity, calamities):
    score = 0
    if ownership.upper() == 'YES':
        score = score + 0
    else:
        score = score + 10
    # number of members in house consideration
    if members == 1 | members == 2:
        score = score + 10 * 2
    elif members == 3:
        score = score + 6 * 2
    elif members == 4 | members == 5:
        score = score + 2 * 2
    else:
        score = score + 0
    # resident area consideration
    if area <= 50:
        score = score + 0
    elif area > 50 & area <= 100:
        score = score + 1 * 1.2
    elif area > 100 & area <= 150:
        score = score + 2 * 1.2
    elif area > 150 & area <= 200:
        score = score + 4 * 1.2
    elif area > 200 & area <= 300:
        score = score + 6 * 1.2
    elif area > 300 & area <= 500:
        score = score + 8 * 1.2
    else:
        score = score + 10 * 1.2
    # water quantity consideration
    if water <= 10:
        score = score + 0
    elif water > 10 & water <= 30:
        score = score + 1 * 1.2
    elif water > 30 & water <= 50:
        score = score + 2 * 1.2
    elif water > 50 & water <= 80:
        score = score + 3 * 1.2
    elif water > 80 & water <= 100:
        score = score + 5 * 1.2
    elif water > 100 & water <= 150:
        score = score + 7 * 1.2
    else:
        score = score + 9 * 1.2
    # roofing considerations
    if roofing == 1:
        score = score + 0
    if roofing == 2:
        score = score + 1
    if roofing == 3:
        score = score + 6
    if roofing == 4:
        score = score + 10
    # number of bathrooms consideration
    if bathrooms == 0:
        score = score + 0
    if bathrooms == 1:
        score = score + 2 * 1.2
    if bathrooms == 2:
        score = score + 4 * 1.2
    if bathrooms == 3:
        score = score + 7 * 1.2
    else:
        score = score + 10 * 1.2
    # electricity in consideration
    if electricity <= 3:
        score = score + 0
    elif electricity > 3 & electricity <= 10:
        score = score + 1 * 1.4
    elif electricity > 10 & electricity <= 16:
        score = score + 3 * 1.4
    elif electricity > 16 & electricity <= 24:
        score = score + 10 * 1.4
    # calamities in considerations
    if calamities.upper() == 'NO':
        score = score + 10
    return score


def get_financial(income, owner, valueposses, healthissues):
    score = 0
    # income per person consideration
    if income <= 2000:
        score = score + 0
    elif income > 2000 & income <= 5000:
        score = score + 1 * 3.5
    elif income > 5000 & income <= 10000:
        score = score + 3 * 3.5
    elif income > 10000 & income <= 14000:
        score = score + 6 * 3.5
    elif income > 14000 & income <= 20000:
        score = score + 7 * 3.5
    elif income > 20000 & income <= 50000:
        score = score + 8 * 3.5
    else:
        score = score + 10 * 3.5
    # ownership consideration
    if owner.upper() == 'NO':
        score = score + 10*1.5
    # health issue
    if healthissues == 0:
        score = score + 10*3.5
    elif healthissues == 1:
        score = score + 3*3.5
    elif healthissues >= 2:
        score = score + 0
    # value of possession
    if valueposses <= 100000:
        score = score + 0
    elif valueposses > 100000 & valueposses <= 300000:
        score = score + 1*1.5
    elif valueposses > 300000 & valueposses <= 700000:
        score = score + 3*1.5
    elif valueposses > 700000 & valueposses <= 1500000:
        score = score + 6*1.5
    elif valueposses > 1500000 & valueposses <= 2500000:
        score = score + 8*1.5
    else:
        score = score + 10*1.5
    return score
