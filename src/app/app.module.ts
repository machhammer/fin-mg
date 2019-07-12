import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';
import {BrowserAnimationsModule} from '@angular/platform-browser/animations';
import { MaterialModule } from './material.module';
import {FlexLayoutModule} from '@angular/flex-layout';
import { GoogleChartsModule } from 'angular-google-charts';

import { AppComponent } from './app.component';
import { LayoutComponent } from './layout/layout.component';
import { HomeComponent } from './home/home.component';
import { RoutingModule } from './routing/routing.module';
import { HeaderComponent } from './navigation/header/header.component';
import { SidenavListComponent } from './navigation/sidenav-list/sidenav-list.component';
import { AccountComponent } from './account/account.component';
import { OwnerComponent } from './owner/owner.component';
import { ContentLayoutComponent } from './content-layout/content-layout.component';

import { ContentCard1Component } from './content/content-card1/content-card1.component';
import { ContentCard2Component } from './content/content-card2/content-card2.component';
import { ContentCard3Component } from './content/content-card3/content-card3.component';
import { ContentCard4Component } from './content/content-card4/content-card4.component';
import { ContentCard5Component } from './content/content-card5/content-card5.component';
import { ContentCard6Component } from './content/content-card6/content-card6.component';

@NgModule({
  declarations: [
    AppComponent,
    LayoutComponent,
    HomeComponent,
    HeaderComponent,
    SidenavListComponent,
    AccountComponent,
    OwnerComponent,
    ContentLayoutComponent,
    ContentCard1Component,
    ContentCard2Component,
    ContentCard3Component,
    ContentCard4Component,
    ContentCard5Component,
    ContentCard6Component
  ],
  imports: [
    BrowserModule,
    BrowserAnimationsModule,
    MaterialModule,
    FlexLayoutModule,
    RoutingModule,
    GoogleChartsModule,
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }