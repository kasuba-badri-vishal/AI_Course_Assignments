Assumptions made

Infected node -- Person infecting with Covid-19 Hypothesis (prior probability)
considerd 
p(Infected=True)  = 0.1

sendQuarintine -- This node decides whether to send a person to quarintine or not

This depends on whether person
1. Has travelled in the Covid-19 hit country (Fly_in_person)
2. Having symptoms of corona (status_health)
3. Already hit by Covid-19 (Infected)

P(sendQuarintine = true / Infected = true) = 1
P(sendQuarintine = true / Infected = false , Fly_in_person = true , status_health = true) = 1
P(sendQuarintine = true / Infected = false , Fly_in_person = true , status_health = false) = 0.7
P(sendQuarintine = true / Infected = false , Fly_in_person = false , status_health = true) = 0.6
P(sendQuarintine = true / Infected = false , Fly_in_person = false , status_health = false) = 0.1

Hospitalized patient's area is also considerd as Quarintine
