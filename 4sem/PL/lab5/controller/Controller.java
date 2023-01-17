package controller;

import java.sql.Statement;
import java.io.IOException;
import java.net.URL;
import java.sql.Connection;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.util.ResourceBundle;
import javafx.collections.FXCollections;
import javafx.collections.ObservableList;
import javafx.event.ActionEvent;
import javafx.event.EventHandler;
import javafx.fxml.FXML;
import javafx.fxml.FXMLLoader;
import javafx.fxml.Initializable;
import javafx.scene.Parent;
import javafx.scene.Scene;
import javafx.scene.control.Button;
import javafx.scene.control.ContextMenu;
import javafx.scene.control.MenuItem;
import javafx.scene.control.TableColumn;
import javafx.scene.control.TableView;
import javafx.scene.control.TextField;
import javafx.scene.control.cell.PropertyValueFactory;
import javafx.scene.input.MouseButton;
import javafx.scene.input.MouseEvent;
import javafx.stage.Modality;
import javafx.stage.Stage;
import database.DB;
import database.city;


public class Controller implements Initializable{

    @FXML
    TableView<city> DB_table; 
    static TableView<city> DB_table_copy;
    @FXML
    TableColumn<city, Integer> columnId;
    @FXML
    TableColumn<city, String> columnName;
    @FXML
    TableColumn<city, Integer> columnArea;
    @FXML
    Button btn_filter;
    @FXML
    TextField textQuery;
    DB db;
    Statement stmt = null;
    Connection con = null;
    ResultSet rs = null;
    ObservableList<city> cities;

    @Override
    public void initialize(URL arg0, ResourceBundle arg1) { 
        cities = FXCollections.observableArrayList();
        columnId.setCellValueFactory(new PropertyValueFactory<city, Integer>("id"));
        columnName.setCellValueFactory(new PropertyValueFactory<city, String>("name"));
        columnArea.setCellValueFactory(new PropertyValueFactory<city, Integer>("area"));
        db = new DB("postgres", "1234");
        con = db.getConnection(); 

        ContextMenu cm = new ContextMenu();
        MenuItem act1 = new MenuItem("Insert");
        cm.getItems().add(act1);
        MenuItem act2 = new MenuItem("Update");
        cm.getItems().add(act2);
        MenuItem act3 = new MenuItem("Delete");
        cm.getItems().add(act3);

        DB_table.addEventHandler(MouseEvent.MOUSE_CLICKED, new EventHandler<MouseEvent>() {

            @Override
            public void handle(MouseEvent click) {
                if(click.getButton() == MouseButton.SECONDARY) {
                    cm.show(DB_table_copy, click.getScreenX(), click.getScreenY());
                }
            }
        });
    
        act1.setOnAction(event -> {
            insert();
        });

        act2.setOnAction(event -> {
            update();
        });
    
        act3.setOnAction(event -> {
            delete();
        });
        DB_table_copy = DB_table;
        refresh();
    }

    public void insert(){
        Stage stage = new Stage();
        Parent root;
        try {
            root = FXMLLoader.load(getClass().getResource(".\\..\\view\\insert.fxml"));
            Scene scene = new Scene(root);
            stage.setScene(scene);
            stage.setTitle("INSERT");
            stage.setResizable(false);
            stage.initModality(Modality.WINDOW_MODAL);
            stage.initOwner(DB_table.getScene().getWindow());
            stage.show();
        } catch (IOException e) {
            e.printStackTrace();
        } 
        refresh();
    }

    public void update(){
        Stage stage = new Stage();
        Parent root;
        try {
            root = FXMLLoader.load(getClass().getResource(".\\..\\view\\update.fxml"));
            Scene scene = new Scene(root);
            stage.setScene(scene);
            stage.setTitle("UPDATE");
            stage.setResizable(false);
            stage.initModality(Modality.WINDOW_MODAL);
            stage.initOwner(DB_table.getScene().getWindow());
            stage.show();
        } catch (IOException e) {
            e.printStackTrace();
        } 
        refresh();
    }

    public void delete(){
        String id = String.valueOf(DB_table_copy.getSelectionModel().getSelectedItem().getId());
        city.deleteCity(id);
        refresh();
    }

    static public void refresh(){
        ObservableList<city> cities = FXCollections.observableArrayList();
        try {
            cities = city.getAllCities();
        } catch (SQLException e) {
            e.printStackTrace();
        }
        DB_table_copy.setItems(cities);
    }

    @FXML
    public void filter(ActionEvent event){
        String query;
        ObservableList<city> cities = FXCollections.observableArrayList();
        query = textQuery.getText();
        if (query.equals("")){
            refresh();
            return;
        }
        try {
            cities = city.getFilteredCities(query);
            DB_table_copy.setItems(cities);
        } catch (Exception e) {
            textQuery.setText("Invalid query");
        }
    }    
}

