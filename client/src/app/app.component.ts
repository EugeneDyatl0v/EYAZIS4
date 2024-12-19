import {Component, OnInit} from '@angular/core';
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
import {Article} from './model/Article';
import {ArticleServiceService} from './service/article-service.service';
import {NgForOf, NgIf} from '@angular/common';
import {MatList, MatListItem, MatListSubheaderCssMatStyler} from '@angular/material/list';
import {MatLine} from '@angular/material/core';
import {MatDivider} from '@angular/material/divider';

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
    RouterOutlet,
    NgForOf,
    MatList,
    MatListSubheaderCssMatStyler,
    MatListItem,
    MatLine,
    MatDivider,
    NgIf
  ],
  templateUrl: './app.component.html',
  styleUrl: './app.component.css'
})
export class AppComponent  implements OnInit{
  articles!: Article[];

  constructor(
    private service: ArticleServiceService
  ) {
  }

  ngOnInit(): void {
    this.service.getAllArticles().subscribe(
      response => {
        this.articles = response.data;
      }
    )
  }
  title = 'client';
}
