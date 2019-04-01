import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';
import { FormsModule } from '@angular/forms';
import { RouterModule, Routes} from '@angular/router';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { SignComponent } from './components/sign/sign.component';
import { MensclothesComponent } from './component/mensclothes/mensclothes.component';

const appRoutes:Routes = [
  {path: '', component:MensclothesComponent},
  {path: 'about', component:SignComponent}
]

@NgModule({
  declarations: [
    AppComponent,
    SignComponent,
    MensclothesComponent
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    FormsModule,
    RouterModule.forRoot(appRoutes)
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
