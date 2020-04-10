import { Component, OnInit } from '@angular/core';
import { AlertService } from '../services/alert.service';
import { UserService } from '../services/user.service';
import { map } from 'rxjs/operators';
import { User } from '../models/user';
import { AuthenticationService } from '../services/authentication.service';
import { Subscription } from 'rxjs';
import { FormControl, FormGroup, Validators, FormBuilder } from '@angular/forms';
import { Router } from '@angular/router';
import { Breakpoints, BreakpointObserver } from '@angular/cdk/layout';


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

  cards = this.breakpointObserver.observe(Breakpoints.Handset).pipe(
    map(({ matches }) => {
      if (matches) {
        return [
          { title: 'Conservative', cols: 2, rows: 1, content: 'hallo1'},
          { title: 'Balanced', cols: 2, rows: 1, content: '' },
          { title: 'Aggressive', cols: 2, rows: 1, content: 'hallo3' },
          { title: 'Tactical Allocation', cols: 2, rows: 1, content: 'hallo4' }
        ];
      }

      return [
        { title: 'Conservative', cols: 1, rows: 1, content: 'hallo5' },
        { title: 'Balanced', cols: 1, rows: 1, content: 'hallo6' },
        { title: 'Aggressive', cols: 1, rows: 1, content: 'hallo7' },
        { title: 'Tactival Allocation', cols: 1, rows: 1, content: 'hallo8' }
      ];
    })
  );


  constructor(    
    private router: Router,
    private userService: UserService,
    private alertService: AlertService,
    private formBuilder: FormBuilder,
    private authenticationService: AuthenticationService,
    private breakpointObserver: BreakpointObserver
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
