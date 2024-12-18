import {Component, Input, OnInit} from '@angular/core';
import {Word} from "../../model/Word";
import {
  MatCell,
  MatCellDef,
  MatColumnDef,
  MatHeaderCell, MatHeaderCellDef,
  MatHeaderRow, MatHeaderRowDef,
  MatRow, MatRowDef,
  MatTable
} from "@angular/material/table";
import {ArticleServiceService} from '../../service/article-service.service';

@Component({
  selector: 'app-article-words-table-words-part-2',
  imports: [
    MatCell,
    MatColumnDef,
    MatHeaderCell,
    MatHeaderRow,
    MatRow,
    MatTable,
    MatCellDef,
    MatHeaderCellDef,
    MatHeaderRowDef,
    MatRowDef
  ],
  templateUrl: './article-words-table-words-part-2.component.html',
  standalone: true,
  styleUrl: './article-words-table-words-part-2.component.css'
})
export class ArticleWordsTableWordsPart2Component implements OnInit {
  @Input() data!: any;
  dataSource!: Word[];
  displayedColumns: string[] = ['word', 'part_of_the_speech_tag', "part_of_the_speech_meaning"];

  constructor(
    private service: ArticleServiceService
  ) {
  }

  ngOnInit(): void {
    this.service.getSpeechParts(this.data)
      .subscribe(
        response => {
          this.dataSource = response.data
        }
      )
  }

  convertTag(partOfTheSpeechTag: string): string {
    return ""
  }
}
