import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { Routes, RouterModule } from '@angular/router';

import { HomeComponent } from '../home/home.component';
import { OwnerComponent } from '../owner/owner.component';
import { ProfileComponent } from '../profile/profile.component';
import { RiskProfileComponent } from '../business/risk-profile/risk-profile.component';
import { LoginComponent } from '../login/login.component';
import { UsersComponent } from '../users/users.component';
import { DashboardComponent } from '../dashboard/dashboard.component';
import { AssetFinderComponent } from '../asset-finder/asset-finder.component';
import { PersonalProfileComponent } from '../personal-profile/personal-profile.component';
import { RegisterComponent } from '../register/register.component';
import { AuthGuard } from '../guards/auth.guard';




const routes: Routes = [
  { path: 'home', component: HomeComponent, canActivate: [AuthGuard]},
  { path: '',   redirectTo: '/home', pathMatch: 'full' },

  { path: 'profile', component: ProfileComponent, canActivate: [AuthGuard]},
  { path: 'risk_profile', component: RiskProfileComponent, canActivate: [AuthGuard]},
  { path: 'dashboard', component: DashboardComponent, canActivate: [AuthGuard]},
  { path: 'asset_finder', component: AssetFinderComponent, canActivate: [AuthGuard]},
  { path: 'personal_profile', component: PersonalProfileComponent, canActivate: [AuthGuard]},
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
