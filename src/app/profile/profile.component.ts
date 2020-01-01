import { Component, OnInit } from '@angular/core';
import { AlertService } from '../services/alert.service';
import { UserService } from '../services/user.service';
import { User } from '../models/user';
import { AuthenticationService } from '../services/authentication.service';
import { Subscription } from 'rxjs';
import { FormControl, FormGroup, Validators, FormBuilder } from '@angular/forms';
import { Router } from '@angular/router';



@Component({
  selector: 'app-profile',
  templateUrl: './profile.component.html',
  styleUrls: ['./profile.component.css']
})
export class ProfileComponent implements OnInit {

  currentUser: User;
  currentUserSubscription: Subscription;

  profileForm: FormGroup;

  username: String;


  constructor(    
    private router: Router,
    private userService: UserService,
    private alertService: AlertService,
    private formBuilder: FormBuilder,
    private authenticationService: AuthenticationService
  ) {
    this.currentUserSubscription = this.authenticationService.currentUser.subscribe(user => {
        this.currentUser = user;
    });

    
  }

  ngOnInit() {  
    this.profileForm = new FormGroup({
      'email': new FormControl(null),
      'firstName': new FormControl(null),
      'lastName': new FormControl(null)
    });
    
  }

  onSubmit() {
    console.log('Your order has been submitted', this.profileForm.value);
  }
 

}
