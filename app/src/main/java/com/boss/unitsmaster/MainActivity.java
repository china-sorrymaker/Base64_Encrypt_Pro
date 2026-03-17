package com.boss.unitsmaster;

import android.os.Bundle;
import android.util.Base64;
import android.widget.Button;
import android.widget.EditText;
import android.widget.TextView;
import androidx.appcompat.app.AppCompatActivity;

public class MainActivity extends AppCompatActivity {
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        EditText etInput = findViewById(R.id.etInput);
        Button btnEncode = findViewById(R.id.btnEncode);
        Button btnDecode = findViewById(R.id.btnDecode);
        Button btnClear = findViewById(R.id.btnClear);
        TextView tvOutput = findViewById(R.id.tvOutput);

        btnEncode.setOnClickListener(v -> {
            String s = etInput.getText().toString();
            if (!s.isEmpty()) {
                tvOutput.setText(Base64.encodeToString(s.getBytes(), Base64.NO_WRAP));
            }
        });

        btnDecode.setOnClickListener(v -> {
            String s = etInput.getText().toString();
            if (!s.isEmpty()) {
                try {
                    tvOutput.setText(new String(Base64.decode(s, Base64.DEFAULT), "UTF-8"));
                } catch (Exception e) {
                    tvOutput.setText(getString(R.string.error_msg));
                }
            }
        });

        btnClear.setOnClickListener(v -> {
            etInput.setText("");
            tvOutput.setText("");
        });
    }
}