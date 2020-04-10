import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';
import { BrowserAnimationsModule } from '@angular/platform-browser/animations';
import { MaterialModule } from './material.module';
import { FlexLayoutModule } from '@angular/flex-layout';
import { GoogleChartsModule } from 'angular-google-charts';
import { ReactiveFormsModule }    from '@angular/forms';
import { FormsModule } from '@angular/forms'
import { DomSanitizer } from '@angular/platform-browser'


import { HttpClientModule, HTTP_INTERCEPTORS } from '@angular/common/http';
import { fakeBackendProvider } from '../app/helpers/fake-backend';
import { JwtInterceptor } from '../app/helpers/jwt.interceptor';
import { ErrorInterceptor } from '../app/helpers/error.interceptor';
import { AppComponent } from './app.component';
import { HomeComponent } from './home/home.component';
import { RoutingModule } from './routing/routing.module';
import { OwnerComponent } from './owner/owner.component';
import { AlertComponent } from './alert/alert.component';
import { UsersComponent } from './users/users.component';
import { LoginComponent } from './login/login.component';
import { RegisterComponent } from './register/register.component';
import { ProfileComponent } from './profile/profile.component';
import { RiskProfileComponent } from './business/risk-profile/risk-profile.component';
import { AppNavComponent } from './app-nav/app-nav.component';
import { LayoutModule } from '@angular/cdk/layout';
import { DashboardComponent } from './dashboard/dashboard.component';
import { AssetFinderComponent } from './asset-finder/asset-finder.component';
import { PersonalProfileComponent } from './personal-profile/personal-profile.component';
import { TabOneComponent } from './dashboard/tab-one/tab-one.component';
import { TabTwoComponent } from './dashboard/tab-two/tab-two.component';

@NgModule({
  declarations: [
    AppComponent,
    HomeComponent,
    OwnerComponent,
    AlertComponent,
    UsersComponent,
    LoginComponent,
    RegisterComponent,
    ProfileComponent,
    RiskProfileComponent,
    AppNavComponent,
    DashboardComponent,
    AssetFinderComponent,
    PersonalProfileComponent,
    TabOneComponent,
    TabTwoComponent
  ],
  imports: [
    BrowserModule,
    BrowserAnimationsModule,
    HttpClientModule,
    ReactiveFormsModule,
    MaterialModule,
    FlexLayoutModule,
    RoutingModule,
    GoogleChartsModule,
    LayoutModule,
    FormsModule

  ],
  providers: [
    { provide: HTTP_INTERCEPTORS, useClass: JwtInterceptor, multi: true },
    { provide: HTTP_INTERCEPTORS, useClass: ErrorInterceptor, multi: true },

    // provider used to create fake backend
    fakeBackendProvider
],
  bootstrap: [AppComponent]
})
export class AppModule { }