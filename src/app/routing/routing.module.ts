import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { Routes, RouterModule } from '@angular/router';
import { HomeComponent } from '../home/home.component';
import { AccountComponent } from '../account/account.component';
import { OwnerComponent } from '../owner/owner.component';
import { ContentLayoutComponent } from '../content-layout/content-layout.component';




const routes: Routes = [
  { path: 'home', component: HomeComponent},
  { path: 'account', component: AccountComponent},
  { path: 'owner', component: OwnerComponent},
  { path: 'content', component: ContentLayoutComponent},
  
  
  
  { path: '', redirectTo: '/home', pathMatch: 'full' }
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
