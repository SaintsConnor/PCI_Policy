print("Welcome to the SAQ quiz. We will determine the SAQ type you need based on your answers to the following questions.\n")

# Question 1: Service Provider
service_provider = input("Are you a service provider (Yes/No)? ")

# Question 2: Storage
if service_provider.lower() == "yes":
    SAQ_Type = "SAQ D for Service Providers"
else:
    card_data_storage = input("Do you store cardholder data (including legacy data) electronically (Yes/No)? ")
    if card_data_storage.lower() == "yes":
        SAQ_Type = "SAQ D for Merchants"
    else:
        SAQ_Type = ""

        # Question 3: E-Commerce
        e_commerce = input("Do you have an e-commerce website (Yes/No)? ")
        if e_commerce.lower() == "yes":
            pci_dss_compliant_provider = input("Do you outsource all elements of payment processing to a PCI DSS compliant provider? (Yes/No)? ")
            if pci_dss_compliant_provider.lower() == "yes":
                SAQ_Type = "SAQ A"
            else:
                payment_outsourced = input("Do you outsource some elements of payment processing (e.g. merchant accepts Direct Post), but not all, and no payment data touches your system (Yes/No)? ")
                if payment_outsourced.lower() == "yes":
                    SAQ_Type = "SAQ A-EP"
                else:
                    SAQ_Type = "SAQ D for Merchants"
            
            # Question 4: Face to Face
        else:
            face_to_face = input("Do you accept card-present transactions where the card is physically swiped or inserted into a terminal (Yes/No)? ")
            if face_to_face.lower() == "yes":
              p2pe = input("Do you accept card-present transactions where it is protected by a listed P2PE Solution (Yes/No)? ")
              if p2pe.lower() == "yes":
                SAQ_Type = "SAQ P2PE"
              else:
                internet_connection = input("Does the payment terminal connect to the internet (Yes/No)? ")
                if internet_connection.lower() == "no":
                    SAQ_Type = "SAQ B"
                else:
                    payment_app = input("Do you use a web browser to go to a service providers 'Virtual Payment Application' (Y/N) ")
                    if payment_app.lower() == "yes":
                        SAQ_Type = "SAQ C-VT"
                    else:
                        PTS_Check = input("Do you accept payments through a PTS Approved Device? (Yes/No) ")
                        if PTS_Check.lower() == "yes":
                          SAQ_Type = "SAQ B-IP"
                        else: 
                          SAQ_Type = "SAQ C"

            # Question 5: MOTO
            else:
                moto = input("Do you process mailorder/telephone order (MOTO) transactions (Yes/No)? ")
                if moto.lower() == "yes":
                  pci_dss_compliant_provider = input("Do you outsource all elements of payment processing to a PCI DSS compliant provider? (Yes/No)? ")
                  if pci_dss_compliant_provider.lower() == "yes":
                    SAQ_Type = "SAQ A"
                  else:
                    internet_connection = input("Does the payment terminal connect to the internet (Yes/No)? ")
                    if internet_connection.lower() == "no":
                     SAQ_Type = "SAQ B"
                    else:
                      payment_app = input("Do you use a web browser to go to a service providers 'Virtual Payment Application' (Y/N) ")
                      if payment_app.lower() == "yes":
                        SAQ_Type = "SAQ C-VT"
                      else:
                        PTS_Check = input("Do you accept payments through a PTS Approved Device? (Yes/No) ")
                        if PTS_Check.lower() == "yes":
                          SAQ_Type = "SAQ B-IP"
                        else: 
                          SAQ_Type = "SAQ C"

print(SAQ_Type)
