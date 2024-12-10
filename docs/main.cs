using System.Collections.Generic;
using System.Windows;

namespace CodeSnippetManager
{
    public partial class MainWindow : Window
    {
        private List<Snippet> snippets = new List<Snippet>();

        public MainWindow()
        {
            InitializeComponent();
            LoadSnippets();
        }

        private void LoadSnippets()
        {
            // Загрузка фрагментов кода из хранилища (например, файла или базы данных)
            snippets.Add(new Snippet { Name = "Example", Description = "Example snippet", Tags = "example", Code = "Console.WriteLine(\"Hello, World!\");" });
            SnippetListView.ItemsSource = snippets;
        }

        private void AddSnippet_Click(object sender, RoutedEventArgs e)
        {
            // Открытие окна для добавления нового фрагмента кода
            var addSnippetWindow = new AddSnippetWindow();
            addSnippetWindow.ShowDialog();
            if (addSnippetWindow.Snippet != null)
            {
                snippets.Add(addSnippetWindow.Snippet);
                SnippetListView.Items.Refresh();
            }
        }

        private void InsertSnippet_Click(object sender, RoutedEventArgs e)
        {
            if (SnippetListView.SelectedItem is Snippet selectedSnippet)
            {
                // Вставка выбранного фрагмента кода в активный редактор
                var dte = (EnvDTE.DTE)System.Runtime.InteropServices.Marshal.GetActiveObject("VisualStudio.DTE");
                var activeDocument = dte.ActiveDocument;
                if (activeDocument != null)
                {
                    var selection = (EnvDTE.TextSelection)activeDocument.Selection;
                    selection.Insert(selectedSnippet.Code, (int)EnvDTE.vsInsertFlags.vsInsertFlagsInsertAtEnd);
                }
            }
        }
    }

    public class Snippet
    {
        public string Name { get; set; }
        public string Description { get; set; }
        public string Tags { get; set; }
        public string Code { get; set; }
    }
}