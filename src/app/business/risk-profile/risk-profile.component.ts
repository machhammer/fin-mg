import {Component, OnInit} from '@angular/core';
import {FormBuilder, FormGroup, Validators} from '@angular/forms';


@Component({
  selector: 'app-risk-profile',
  templateUrl: './risk-profile.component.html',
  styleUrls: ['./risk-profile.component.css']
})


export class RiskProfileComponent implements OnInit {
  isLinear = false;
  firstStepFormGroup: FormGroup;
  secondStepFormGroup: FormGroup;
  thirdStepFormGroup: FormGroup;

  constructor(private _formBuilder: FormBuilder) {}

  ngOnInit() {
    this.firstStepFormGroup = this._formBuilder.group({
      firstCtrl: ['', Validators.required]
    });
    this.secondStepFormGroup = this._formBuilder.group({
      secondCtrl: ['', Validators.required]
    });
    this.thirdStepFormGroup = this._formBuilder.group({
      thirdCtrl: ['', Validators.required]
    });
  }
}
