# -*- coding: utf-8 -*-
"""
Created on Sun Nov 29 20:40:35 2020

@author: Home
"""

from flask import Flask, request, render_template
from flask_cors import cross_origin
import sklearn
import pickle
import pandas as pd

app=Flask(__name__)
model = pickle.load(open("flight_model.pkl", "rb"))
@app.route("/")
@cross_origin()
def home():
    return render_template("home.html")
@app.route("/predict", methods = ["GET", "POST"])
@cross_origin()
def predict():
    if request.method == "POST":

        # Date_of_Journey
        date_of_departure = request.form["Dep_Time"]
        Day_of_journey = int(pd.to_datetime(date_of_departure, format="%Y-%m-%dT%H:%M").day)
        Month_of_journey = int(pd.to_datetime(date_of_departure, format ="%Y-%m-%dT%H:%M").month)
        # print("Journey Date : ",Journey_day, Journey_month)

        # Departure
        Departure_hour = int(pd.to_datetime(date_of_departure, format ="%Y-%m-%dT%H:%M").hour)
        Departure_minute = int(pd.to_datetime(date_of_departure, format ="%Y-%m-%dT%H:%M").minute)
        # print("Departure : ",Dep_hour, Dep_min)

        # Arrival
        date_of_arrival = request.form["Arrival_Time"]
        Arrival_hour = int(pd.to_datetime(date_of_arrival, format ="%Y-%m-%dT%H:%M").hour)
        Arrival_minute = int(pd.to_datetime(date_of_arrival, format ="%Y-%m-%dT%H:%M").minute)
        # print("Arrival : ", Arrival_hour, Arrival_min)

        # Duration
        time_dur_hour = abs(Arrival_hour - Departure_hour)
        time_dur_minute = abs(Arrival_minute - Departure_minute)
        # print("Duration : ", dur_hour, dur_min)

        # Total Stops
        Stops_Total = int(request.form["stops"])
        # print(Total_stops)

        # Airline
        # AIR ASIA = 0 (not in column)
        chossen_airline=request.form['airline']
        if(chossen_airline=='Jet Airways'):
            Jet_Airways = 1
            IndiGo = 0
            Air_India = 0
            Multiple_carriers = 0
            SpiceJet = 0
            Vistara = 0
            GoAir = 0
            Multiple_carriers_Premium_economy = 0
            Jet_Airways_Business = 0
            Vistara_Premium_economy = 0
            Trujet = 0 

        elif (chossen_airline=='IndiGo'):
            Jet_Airways = 0
            IndiGo = 1
            Air_India = 0
            Multiple_carriers = 0
            SpiceJet = 0
            Vistara = 0
            GoAir = 0
            Multiple_carriers_Premium_economy = 0
            Jet_Airways_Business = 0
            Vistara_Premium_economy = 0
            Trujet = 0 

        elif (chossen_airline=='Air India'):
            Jet_Airways = 0
            IndiGo = 0
            Air_India = 1
            Multiple_carriers = 0
            SpiceJet = 0
            Vistara = 0
            GoAir = 0
            Multiple_carriers_Premium_economy = 0
            Jet_Airways_Business = 0
            Vistara_Premium_economy = 0
            Trujet = 0 
            
        elif (chossen_airline=='Multiple carriers'):
            Jet_Airways = 0
            IndiGo = 0
            Air_India = 0
            Multiple_carriers = 1
            SpiceJet = 0
            Vistara = 0
            GoAir = 0
            Multiple_carriers_Premium_economy = 0
            Jet_Airways_Business = 0
            Vistara_Premium_economy = 0
            Trujet = 0 
            
        elif (chossen_airline=='SpiceJet'):
            Jet_Airways = 0
            IndiGo = 0
            Air_India = 0
            Multiple_carriers = 0
            SpiceJet = 1
            Vistara = 0
            GoAir = 0
            Multiple_carriers_Premium_economy = 0
            Jet_Airways_Business = 0
            Vistara_Premium_economy = 0
            Trujet = 0 
            
        elif (chossen_airline=='Vistara'):
            Jet_Airways = 0
            IndiGo = 0
            Air_India = 0
            Multiple_carriers = 0
            SpiceJet = 0
            Vistara = 1
            GoAir = 0
            Multiple_carriers_Premium_economy = 0
            Jet_Airways_Business = 0
            Vistara_Premium_economy = 0
            Trujet = 0

        elif (chossen_airline=='GoAir'):
            Jet_Airways = 0
            IndiGo = 0
            Air_India = 0
            Multiple_carriers = 0
            SpiceJet = 0
            Vistara = 0
            GoAir = 1
            Multiple_carriers_Premium_economy = 0
            Jet_Airways_Business = 0
            Vistara_Premium_economy = 0
            Trujet = 0

        elif (chossen_airline=='Multiple carriers Premium economy'):
            Jet_Airways = 0
            IndiGo = 0
            Air_India = 0
            Multiple_carriers = 0
            SpiceJet = 0
            Vistara = 0
            GoAir = 0
            Multiple_carriers_Premium_economy = 1
            Jet_Airways_Business = 0
            Vistara_Premium_economy = 0
            Trujet = 0

        elif (chossen_airline=='Jet Airways Business'):
            Jet_Airways = 0
            IndiGo = 0
            Air_India = 0
            Multiple_carriers = 0
            SpiceJet = 0
            Vistara = 0
            GoAir = 0
            Multiple_carriers_Premium_economy = 0
            Jet_Airways_Business = 1
            Vistara_Premium_economy = 0
            Trujet = 0

        elif (airline=='Vistara Premium economy'):
            Jet_Airways = 0
            IndiGo = 0
            Air_India = 0
            Multiple_carriers = 0
            SpiceJet = 0
            Vistara = 0
            GoAir = 0
            Multiple_carriers_Premium_economy = 0
            Jet_Airways_Business = 0
            Vistara_Premium_economy = 1
            Trujet = 0
            
        elif (chossen_airline=='Trujet'):
            Jet_Airways = 0
            IndiGo = 0
            Air_India = 0
            Multiple_carriers = 0
            SpiceJet = 0
            Vistara = 0
            GoAir = 0
            Multiple_carriers_Premium_economy = 0
            Jet_Airways_Business = 0
            Vistara_Premium_economy = 0
            Trujet = 1

        else:
            Jet_Airways = 0
            IndiGo = 0
            Air_India = 0
            Multiple_carriers = 0
            SpiceJet = 0
            Vistara = 0
            GoAir = 0
            Multiple_carriers_Premium_economy = 0
            Jet_Airways_Business = 0
            Vistara_Premium_economy = 0
            Trujet = 0

        # print(Jet_Airways,
        #     IndiGo,
        #     Air_India,
        #     Multiple_carriers,
        #     SpiceJet,
        #     Vistara,
        #     GoAir,
        #     Multiple_carriers_Premium_economy,
        #     Jet_Airways_Business,
        #     Vistara_Premium_economy,
        #     Trujet)

        # Source
        # Banglore = 0 (not in column)
        Source = request.form["Source"]
        if (Source == 'Delhi'):
            source_Delhi = 1
            source_Kolkata = 0
            source_Mumbai = 0
            source_Chennai = 0

        elif (Source == 'Kolkata'):
            source_Delhi = 0
            source_Kolkata = 1
            source_Mumbai = 0
            source_Chennai = 0

        elif (Source == 'Mumbai'):
            source_Delhi = 0
            source_Kolkata = 0
            source_Mumbai = 1
            source_Chennai = 0

        elif (Source == 'Chennai'):
            source_Delhi = 0
            source_Kolkata = 0
            source_Mumbai = 0
            source_Chennai = 1

        else:
            source_Delhi = 0
            source_Kolkata = 0
            source_Mumbai = 0
            source_Chennai = 0

        # print(s_Delhi,
        #     s_Kolkata,
        #     s_Mumbai,
        #     s_Chennai)

        # Destination
        # Banglore = 0 (not in column)
        Destination = request.form["Destination"]
        if (Destination == 'Cochin'):
            destination_Cochin = 1
            destination_Delhi = 0
            destination_New_Delhi = 0
            destination_Hyderabad = 0
            destination_Kolkata = 0
        
        elif (Destination == 'Delhi'):
            destination_Cochin = 0
            destination_Delhi = 1
            destination_New_Delhi = 0
            destination_Hyderabad = 0
            destination_Kolkata = 0

        elif (Destination == 'New_Delhi'):
            destination_Cochin = 0
            destination_Delhi = 0
            destination_New_Delhi = 1
            destination_Hyderabad = 0
            destination_Kolkata = 0

        elif (Destination == 'Hyderabad'):
            destination_Cochin = 0
            destination_Delhi = 0
            destination_New_Delhi = 0
            destination_Hyderabad = 1
            destination_Kolkata = 0

        elif (Destination == 'Kolkata'):
            destination_Cochin = 0
            destination_Delhi = 0
            destination_New_Delhi = 0
            destination_Hyderabad = 0
            destination_Kolkata = 1

        else:
            destination_Cochin = 0
            destination_Delhi = 0
            destination_New_Delhi = 0
            destination_Hyderabad = 0
            destination_Kolkata = 0

        # print(
        #     d_Cochin,
        #     d_Delhi,
        #     d_New_Delhi,
        #     d_Hyderabad,
        #     d_Kolkata
        # )
        

    #     ['Total_Stops', 'Journey_day', 'Journey_month', 'Dep_hour',
    #    'Dep_min', 'Arrival_hour', 'Arrival_min', 'Duration_hours',
    #    'Duration_mins', 'Airline_Air India', 'Airline_GoAir', 'Airline_IndiGo',
    #    'Airline_Jet Airways', 'Airline_Jet Airways Business',
    #    'Airline_Multiple carriers',
    #    'Airline_Multiple carriers Premium economy', 'Airline_SpiceJet',
    #    'Airline_Trujet', 'Airline_Vistara', 'Airline_Vistara Premium economy',
    #    'Source_Chennai', 'Source_Delhi', 'Source_Kolkata', 'Source_Mumbai',
    #    'Destination_Cochin', 'Destination_Delhi', 'Destination_Hyderabad',
    #    'Destination_Kolkata', 'Destination_New Delhi']
        
        prediction=model.predict([[
            Stops_Total,
            Day_of_journey,
            Month_of_journey,
            Departure_hour,
            Departure_minute,
            Arrival_hour,
            Arrival_minute,
            time_dur_hour,
            time_dur_minute,
            Air_India,
            GoAir,
            IndiGo,
            Jet_Airways,
            Jet_Airways_Business,
            Multiple_carriers,
            Multiple_carriers_Premium_economy,
            SpiceJet,
            Trujet,
            Vistara,
            Vistara_Premium_economy,
            source_Chennai,
            source_Delhi,
            source_Kolkata,
            source_Mumbai,
            destination_Cochin,
            destination_Delhi,
            destination_Hyderabad,
            destination_Kolkata,
            destination_New_Delhi
        ]])

        output=round(prediction[0],2)

        return render_template('home.html',prediction_text="Your Flight price is Rs. {}".format(output))


    return render_template("home.html")




if __name__ == "__main__":
    app.run(debug=True)
