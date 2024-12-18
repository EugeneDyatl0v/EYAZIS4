import {Component, Input, OnInit} from '@angular/core';
import {MatCard, MatCardHeader, MatCardModule} from "@angular/material/card";
import {Article} from '../../model/Article';
import {ArticleServiceService} from '../../service/article-service.service';

@Component({
    selector: 'app-article-text',
    imports: [
        MatCard,
        MatCardModule,
        MatCardHeader
    ],
    templateUrl: './article-text.component.html',
    standalone: true,
    styleUrl: './article-text.component.css'
})
export class ArticleTextComponent implements OnInit{
    @Input() data: any;
    article!: Article;

  constructor(private service: ArticleServiceService) {
  }

  ngOnInit(): void {
    this.service.getArticle(this.data)
      .subscribe(
        response => {
          this.article = response.data;
        }
      )
  }

}
