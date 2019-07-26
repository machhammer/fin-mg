import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { Routes, RouterModule } from '@angular/router';
import { HomeComponent } from '../home/home.component';
import { AccountComponent } from '../account/account.component';
import { OwnerComponent } from '../owner/owner.component';
import { ProfileComponent } from '../profile/profile.component';

import { ContentLayoutComponent } from '../content-layout/content-layout.component';
import { ContentCard1Component } from '../content/content-card1/content-card1.component';
import { ContentCard2Component } from '../content/content-card2/content-card2.component';
import { ContentCard3Component } from '../content/content-card3/content-card3.component';
import { ContentCard4Component } from '../content/content-card4/content-card4.component';
import { ContentCard5Component } from '../content/content-card5/content-card5.component';
import { ContentCard6Component } from '../content/content-card6/content-card6.component';
import { LoginComponent } from '../login/login.component';
import { UsersComponent } from '../users/users.component';

import { RegisterComponent } from '../register/register.component';
import { AuthGuard } from '../guards/auth.guard';




const routes: Routes = [
  { path: 'home', component: HomeComponent, canActivate: [AuthGuard]},
  { path: '',   redirectTo: '/home', pathMatch: 'full' },

  { path: 'account', component: AccountComponent, canActivate: [AuthGuard]},
  { path: 'profile', component: ProfileComponent, canActivate: [AuthGuard]},
   
  { path: 'content', component: ContentLayoutComponent, canActivate: [AuthGuard],
    children:
    [
      { path: 'card1', component: ContentCard1Component, outlet: 'out1'},
      { path: 'card2', component: ContentCard2Component, outlet: 'out2'},
      { path: 'card3', component: ContentCard3Component, outlet: 'out3'},
      { path: 'card4', component: ContentCard4Component, outlet: 'out4'},
      { path: 'card5', component: ContentCard5Component, outlet: 'out5'},
      { path: 'card6', component: ContentCard6Component, outlet: 'out6'},
      
    ],
  },
  { path: 'login', component: LoginComponent },
  { path: 'register', component: RegisterComponent },
  { path: 'list', component: UsersComponent },
  
  
];

@NgModule({
  imports: [
    CommonModule,
    RouterModule.forRoot(routes)
  ],
  exports: [
    RouterModule
  ],
  declarations: []
})
export class RoutingModule { }
