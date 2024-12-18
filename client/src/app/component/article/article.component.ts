import {Component, OnInit} from '@angular/core';
import {MatTab, MatTabGroup} from "@angular/material/tabs";
import {ArticleTextComponent} from "../article-text/article-text.component";
import {ActivatedRoute, RouterModule} from "@angular/router";
import {ArticleWordsTableComponent} from "../article-words-table/article-words-table.component";
import {ArticleWordsTableWordsPart2Component} from "../article-words-table-words-part-2/article-words-table-words-part-2.component";
import {ArticleSentencesComponent} from "../article-sentences/article-sentences.component";

@Component({
    selector: 'app-article',
    imports: [
        MatTabGroup,
        MatTab,
        RouterModule,
        ArticleTextComponent,
        ArticleWordsTableComponent,
        ArticleWordsTableWordsPart2Component,
        ArticleSentencesComponent
    ],
    templateUrl: './article.component.html',
    standalone: true,
    styleUrl: './article.component.css'
})
export class ArticleComponent implements OnInit{

    articleId: string | null = "";

    constructor(private route: ActivatedRoute) { }

    ngOnInit(): void {
        this.route.paramMap.subscribe(params => {
            this.articleId = params.get('id');
            console.log("test " + this.articleId);
        });
    }

}
