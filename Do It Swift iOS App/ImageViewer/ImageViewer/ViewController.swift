//
//  ViewController.swift
//  ImageViewer
//
//  Created by 전기범 on 2022/09/16.
//

import UIKit

class ViewController: UIViewController {
    var maxImg = 6
    var presentImg = 1
    
    @IBOutlet var imgViewer: UIImageView!
    
    override func viewDidLoad() {
        super.viewDidLoad()
        // Do any additional setup after loading the view.
    }
    
    @IBAction func btnPrev(_ sender: UIButton) {
        presentImg-=1
        if (presentImg<1){
            presentImg=maxImg
        }
        let imgName = "Img/" + String(presentImg) + ".png"
        imgViewer.image = UIImage(named: imgName)
        
        // print(imgName) 이미지 순서 확인용
    }
    
    @IBAction func btnNext(_ sender: UIButton) {
        presentImg+=1
        if (presentImg>maxImg){
            presentImg=1
        }
        let imgName = "Img/" + String(presentImg) + ".png"
        imgViewer.image = UIImage(named: imgName)
        
        // print(imgName)
    }
}

