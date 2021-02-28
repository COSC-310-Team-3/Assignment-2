import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.io.*;
import java.util.*;
import javax.swing.*;


public class Bot extends JFrame{
	private JTextArea Chatarea = new JTextArea();
	private JTextField Chatfield = new JTextField();
	
	public Bot() {
		JFrame frame = new JFrame();
		frame.setDefaultCloseOperation(EXIT_ON_CLOSE);
		frame.setVisible(true);
		frame.setResizable(false);
		frame.setLayout(null);
		frame.setSize(500, 500);
		frame.setTitle("Sports Bot");
		frame.add(Chatarea);
		frame.add(Chatfield);
		//Text area
		Chatarea.setSize(400, 300);
		Chatarea.setLocation(2, 2);
		//Textfield
		Chatfield.setSize(400, 30);
		Chatfield.setLocation(2, 300);
		
		Chatfield.addActionListener(new ActionListener() {

			@Override
			public void actionPerformed(ActionEvent arg0) {
				String text = Chatfield.getText();
				Chatarea.append("User: " + text + "\n");
				Chatfield.setText("");
				
				if(text.contains("hello") || text.contains("hi")) {
					Bot("Hello, what do you like most hockey, basketball, football or Soccer?");
				}else if(text.contains("Hockey")) {
					Bot("Nice! My favourite player is Loui Erikkson. Who's is your favourite player?");
				}else if(text.contains("Basketball")) {
					
				}else if(text.contains("Football")) {
					
				}
				
				
				else {
					Bot("I didnt understand you, could you repeat that?");
				}
				
				
			}
			
		});
	}
	private void Bot(String Bottext) {
		Chatarea.append("Sports Bot: " + Bottext + "\n");
	}
	
	public static void main(String[] args) {
		new Bot();
		
		
		
	}

}
