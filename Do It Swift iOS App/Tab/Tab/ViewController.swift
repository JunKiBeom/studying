//
//  ViewController.swift
//  Tab
//
//  Created by 전기범 on 2022/09/27.
//

import UIKit

class ViewController: UIViewController {

    override func viewDidLoad() {
        super.viewDidLoad()
        // Do any additional setup after loading the view.
    }
    @IBAction func btnMoveImageView(_ sender: UIButton){
        tabBarController?.selectedIndex = 1
    }
    @IBAction func btnMoveDatePickerView(_ sender: UIButton){
        tabBarController?.selectedIndex = 2
    }
}

