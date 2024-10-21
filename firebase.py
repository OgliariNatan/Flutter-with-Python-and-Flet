# -*- coding: utf-8 -*-

import flet as ft
import pyrebase


firebaseConfig = {
  "apiKey": "AIzaSyAn3SvYnMIWxmu4Vt1XorsEUR_E4wqgy80",
  "authDomain": "exemplo-teste-b9336.firebaseapp.com",
  "projectId": "exemplo-teste-b9336",
  "databaseURL": "https:exemplo-teste.firebaseio.com",
  "storageBucket": "exemplo-teste-b9336.appspot.com",
  "messagingSenderId": "1017608586195",
  "appId": "1:1017608586195:web:a10bf65ba85dc32190a526",
  "measurementId": "G-LE71SEWKHS"
}

firebase = pyrebase.initialize_app(firebaseConfig)
auth = firebase.auth()