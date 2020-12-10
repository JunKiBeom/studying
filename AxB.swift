//
//  main.swift
//  Swift_Commd
//
//  Created by 전기범 on 2020/08/06.
//  Copyright © 2020 전기범. All rights reserved.
//

import Foundation

print("Input Number ex : 1 2")

let a = readLine()?.split(separator: " ").map{Int($0)!}

var sol = Int(a![0]) * Int(a![1])

print(sol)