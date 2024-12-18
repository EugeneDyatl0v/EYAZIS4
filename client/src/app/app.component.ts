import { Component } from '@angular/core';
import {BrowserModule} from "@angular/platform-browser";
import {BrowserAnimationsModule} from "@angular/platform-browser/animations";
import {MatToolbarModule} from "@angular/material/toolbar";
import {RouterModule, RouterOutlet} from "@angular/router";
import {MatIcon} from "@angular/material/icon";
import {MatIconButton} from "@angular/material/button";
import {MatDrawer, MatDrawerContainer} from "@angular/material/sidenav";
import {ArticleComponent} from "./component/article/article.component";
import {ArticleTextComponent} from "./component/article-text/article-text.component";
import {HttpClientModule} from '@angular/common/http';

@Component({
  selector: 'app-root',
  standalone: true,
    imports: [
        MatToolbarModule,
        RouterModule,
        MatIcon,
        MatIconButton,
        MatDrawerContainer,
        MatDrawer,
        ArticleComponent,
        ArticleTextComponent,
        HttpClientModule,
        RouterOutlet
    ],
  templateUrl: './app.component.html',
  styleUrl: './app.component.css'
})
export class AppComponent {
  title = 'client';
}
