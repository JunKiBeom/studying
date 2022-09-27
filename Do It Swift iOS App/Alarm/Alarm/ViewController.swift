//
//  ViewController.swift
//  Alarm
//
//  Created by 전기범 on 2022/09/20.
//

import UIKit

class ViewController: UIViewController {
    let timeSelector : Selector = #selector(ViewController.updateTime)
    let interval = 1.0
    var count = 0
    var alarmTime : String?
    var alarmFlag = false
    
    @IBOutlet var lblCurrentTime: UILabel!
    @IBOutlet var lblSelectTime: UILabel!

    override func viewDidLoad() {
        super.viewDidLoad()
        // Do any additional setup after loading the view.
        Timer.scheduledTimer(timeInterval: interval, target: self, selector: timeSelector, userInfo: nil, repeats: true)
    }
    @IBAction func changeDatePicker(_ sender: UIDatePicker) {
        let datePickerViwe = sender
        
        let formatter = DateFormatter()
        formatter.dateFormat = "yyyy-MM-dd HH:mm EEE"
        lblSelectTime.text = "선택시간 : " + formatter.string(from: datePickerViwe.date)
        formatter.dateFormat = "HH:mm aaa"
        alarmTime = formatter.string(from: datePickerViwe.date)
    }
    
    @objc func updateTime() {
        let date = NSDate()
        
        let formatter = DateFormatter()
        formatter.dateFormat = "yyyy-MM-dd HH:mm EEE"
        lblCurrentTime.text = "현재 시간 : " + formatter.string(from: date as Date)
        
        formatter.dateFormat = "HH:mm aaa"
        let currentTime = formatter.string(from: date as Date)
        if (alarmTime == currentTime) {
            if !alarmFlag {
                let alarmOnAlert = UIAlertController(title: "알림", message: "설정된 시간입니다", preferredStyle: UIAlertController.Style.alert)
                let onAction = UIAlertAction(title: "OK", style: UIAlertAction.Style.default, handler: nil)
                alarmOnAlert.addAction(onAction)
                present(alarmOnAlert, animated: true, completion: nil)
                alarmFlag = true
            }
        }
        else {
            alarmFlag = false
        }
    }
}
