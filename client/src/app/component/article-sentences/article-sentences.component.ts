import {Component, Input, OnInit} from '@angular/core';
import {
  MatAccordion,
  MatExpansionPanel,
  MatExpansionPanelHeader,
  MatExpansionPanelTitle
} from "@angular/material/expansion";
import {Sentence} from "../../model/Sentence";
import {NgForOf} from "@angular/common";
import {DomSanitizer} from "@angular/platform-browser";
import {ArticleServiceService} from '../../service/article-service.service';

@Component({
    selector: 'app-article-sentences',
  imports: [
    MatExpansionPanelTitle,
    MatExpansionPanelHeader,
    MatExpansionPanel,
    MatAccordion,
    NgForOf
  ],
    templateUrl: './article-sentences.component.html',
    standalone: true,
    styleUrl: './article-sentences.component.css'
})
export class ArticleSentencesComponent implements OnInit{
    @Input() data!: any;
    dataSource!: Sentence[];

    constructor(
      private sanitizer: DomSanitizer,
      private articleService: ArticleServiceService
    ) {}

    ngOnInit(): void {
      this.articleService.getSyntax(this.data).subscribe(
        response => {
          this.dataSource = response.data
        }
      )
    }

    getImage(image: string) {
        return this.sanitizer.bypassSecurityTrustHtml(image);
    }
}
